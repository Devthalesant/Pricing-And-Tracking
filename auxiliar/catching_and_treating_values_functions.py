from pymongo import MongoClient
import pandas as pd
import re

# Função para obter dados do MongoDB
def get_dataframe_from_mongodb(collection_name, database_name, query={}):
    print(f"Fetching data from {database_name} : {collection_name}")
    client = MongoClient("sua_string_de_conexão")  # Use sua string de conexão
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


# Função para extrair informações
def extract_quote_items(row):
    items = []
    for item in row['quote_items'].split(';'):
        item = item.strip()  # TIRA SPACE
        if item:
            match = re.match(r'^(.*) \(Qty:\s*(\d+),\s*Amount:\s*(\d+),\s*discountAmount:\s*(\d+)\)', item)

            if match:
                item_name = match.group(1)  # Nome do item
                qty = match.group(2)  # Quantidade
                amount = match.group(3)  # Valor
                discount_amount = match.group(4)  # Desconto

                items.append({
                    'item_name': item_name,
                    'quantity': int(qty),
                    'item-amount': int(amount),
                    'discount_amount': int(discount_amount)
                })

    return items

# Função para tratar valores
def treating_values(billcharges_df):
    # Remover duplicatas de quote_ID
    billcharges_df.drop_duplicates(subset=['quote_id'], keep='first', inplace=True)

    rows = []
    for _, row in billcharges_df.iterrows():
        extracted_items = extract_quote_items(row)
        rows.extend(extracted_items)

    new_df = pd.DataFrame(rows)

    # Filtrar colunas
    columns = ['customer_id', 'quote_id', 'date', 'store_name', 'item_name', 'quantity',
               'item-amount', 'discount_amount', 'payment_method', 'installments', 'total_amount', 'is_paid', 'status']

    new_df = new_df[columns]

    # Renomear colunas
    new_df.rename(columns={'customer_id': 'ID CLIENTE', 'quote_id': 'ID ORÇAMENTO', 'store_name': 'UNIDADE',
                           'item_name': "PROCEDIMENTO", 'quantity': 'QUANTIDADE', 'item-amount': 'VALOR TABELA',
                           'discount_amount': 'DISCONTO ITEM', 'payment_method': 'FORMA DE PAGAMENTO', 'installments': 'PARCELAS',
                           'is_paid': 'PAGO?', 'total_amount': 'TOTAL DO ORÇAMENTO', "date": "DATA", "status": "STATUS"}, inplace=True)

    # Verifique se `bring_dictionaries()` é implementado
    custos_dict, Sales_dic, Appointments_dic, duration_dic, Month_dic = bring_dictionaries()

    # Continuar com o processamento...

    return new_df
