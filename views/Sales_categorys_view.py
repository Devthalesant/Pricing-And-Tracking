import streamlit as st
import pandas as pd

# Here i wanna show the evolution of Sales Costs of Sales and serve, contribuition margin, ...

df_sales_path = "base_de_dados/sales/Sales_View/Cópia de data_sales_2024_updated.csv"
df_sales = pd.read_csv(df_sales_path)

df_sales = df_sales.loc[df_sales['CORTESIA'] != True]
groupby_for_sales = df_sales.groupby(["Unidade", "Grupo", "Mês venda", "Grupo"]).agg({"Valor liquido item": "sum","Quantidade" : "sum",
                                                                                      "Valor tabela item" : "sum", "Custo Direto" : "sum"}).reset_index()


st.dataframe(groupby_for_sales)
