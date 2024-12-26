from pymongo import MongoClient, UpdateOne
import pandas as pd
# Function to get data from Mongo

def get_dataframe_from_mongodb(collection_name, database_name, query={}):

    print(f"Fetching data from {database_name} : {collection_name}")
    client = MongoClient(f"mongodb+srv://rpdprocorpo:iyiawsSCfCsuAzOb@cluster0.lu6ce.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client[database_name]
    collection = db[collection_name]

    data = list(collection.find(query))

    if data:
        dataframe = pd.DataFrame(data)
        if '_id' in dataframe.columns:
            dataframe = dataframe.drop(columns=['_id'])
    else:
        dataframe = pd.DataFrame()

    print(f"Fetched {len(dataframe)} records from {database_name} : {collection_name}")
    return dataframe

# Function to extract the informations at the quote_itens
def extract_quote_items(row):
    items = []
    # Ajustando a regex para capturar corretamente todos os elementos
    for item in row['quote_items'].split(';'):
        item = item.strip() # TIRA SPACE
        if item:
            match = re.match(r'^(.*) \(Qty:\s*(\d+),\s*Amount:\s*(\d+),\s*discountAmount:\s*(\d+)\)', item)

            # See if it matched correctly
            if match:
                item_name = match.group(1)     # Nome do item
                qty = match.group(2)            # Quantidade
                amount = match.group(3)         # Valor (Amount)
                discount_amount = match.group(4) # Desconto

                # # Debugging - print the matched values
                # print("Matched:", item_name, qty, amount, discount_amount)

                items.append({
                    'item_name': item_name,
                    'quantity': int(qty),
                    'item-amount': int(amount),               # Convertendo para inteiro
                    'discount_amount': int(discount_amount), # Convertendo para inteiro
                    **{col: row[col] for col in billcharges_df.columns if col != 'quote_items'}
                })

    return items

     # function that calls the treated updated dataframe

def treating_values():
  # Aplicar a função para cada linha do DataFrame
  rows = []
  for _, row in billcharges_df.iterrows():
      extracted_items = extract_quote_items(row)
      rows.extend(extracted_items)

  # Criar um novo DataFrame com os dados extraídos
  new_df = pd.DataFrame(rows)

  #chosing the columns that i will use
  columns = ['customer_id', 'quote_id','date', 'store_name', 'item_name', 'quantity',
            'item-amount','discount_amount', 'payment_method','installments','total_amount','is_paid',
            'status']

  new_df = new_df[columns]

  #renaming these columns
  new_df.rename(columns={'customer_id': 'ID CLIENTE','quote_id':'ID ORÇAMENTO','store_name': 'UNIDADE',
                        'item_name' : "PROCEDIMENTO",'quantity':'QUANTIDADE','item-amount':'VALOR TABELA',
                        'discount_amount':'DISCONTO ITEM','payment_method': 'FORMA DE PAGAMENTO','installments':'PARCELAS',
                        'is_paid':'PAGO?','total_amount' : 'TOTAL DO ORÇAMENTO',"date" : "DATA","status" : "STATUS" }, inplace=True)

  #bringing all dictionaries for the code
  custos_dict, Sales_dic, Appointments_dic, duration_dic, Month_dic = bring_dictionaries()

  #Maapping all the information from dictionaries:
  new_df["PROCEDIMENTO PADRONIZADO"] = new_df["PROCEDIMENTO"].map(Sales_dic)
                                                                  #x recives eache line of proceduere(lambda x); acess the custos dic
                                                                  #with 2 keys (first is x(name os procedeure) and de secoind is 'CUSTO DIRETO')
                                                                  # IF OR ELSE TO VALIDATE IF THERE IS A VALUE FOR THOSE KEYS
  new_df['CUSTO DIRETO'] = new_df['PROCEDIMENTO PADRONIZADO'].map(lambda x: custos_dict[x]['CUSTO DIRETO'] if x in custos_dict else None)
  new_df['GRUPO'] = new_df["PROCEDIMENTO PADRONIZADO"].map(lambda x: custos_dict[x]["GRUPO"] if x in custos_dict else None)

  new_df['CUSTO DIRETO'] = new_df["CUSTO DIRETO"] * new_df["QUANTIDADE"]

  # Treating the financial values (/100)
  new_df['VALOR TABELA'] = new_df['VALOR TABELA'] / 100
  new_df['DISCONTO ITEM'] = new_df['DISCONTO ITEM'] / 100
  new_df['TOTAL DO ORÇAMENTO'] = new_df['TOTAL DO ORÇAMENTO'] / 100

  # Creating the column total Item :
  new_df["TOTAL ITEM"] = new_df['VALOR TABELA'] * new_df["QUANTIDADE"]

  #TRATING THE DATE VALUS
  new_df["DATA"] = pd.to_datetime(new_df["DATA"])

  #creating the month column
  new_df["MÊS"] = new_df["DATA"].dt.month
  new_df["MÊS"] = new_df["MÊS"].map(Month_dic)

  #Creating colums net total item
  new_df["TOTAL LÍQUIDO ITEM"] = new_df["TOTAL ITEM"] - new_df["DISCONTO ITEM"]

  # defining credit card costs, taxes and commissions

  taxes = 0.1425
  comission = 0.04
  credit_costs = 0.0818 #medain of 7 instalments
  other_costs = taxes + comission + credit_costs

  new_df["CUSTO TOTAL DIRETO ITEM"] = new_df["CUSTO DIRETO"] + (new_df["TOTAL ITEM"] * other_costs)
  new_df

  #reorganizing the columns:
  columns = ['ID CLIENTE','ID ORÇAMENTO','DATA',"MÊS",'UNIDADE',"GRUPO","PROCEDIMENTO","PROCEDIMENTO PADRONIZADO",
            'QUANTIDADE','VALOR TABELA','TOTAL ITEM','DISCONTO ITEM','TOTAL LÍQUIDO ITEM','CUSTO TOTAL DIRETO ITEM','TOTAL DO ORÇAMENTO',
            "CUSTO DIRETO",'FORMA DE PAGAMENTO','PARCELAS','PAGO?',"STATUS"]

  new_df = new_df[columns]

  return new_df
