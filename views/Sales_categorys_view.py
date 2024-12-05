import streamlit as st
import pandas as pd

Month_list = ["Anual","Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
branch_list = ["TODAS","ALPHAVILLE","BELO HORIZONTE","CAMPINAS","COPACABANA","IPIRANGA","ITAIM","JARDINS","LAPA","LONDRINA","MOEMA","MOOCA","OSASCO",
               "RIBEIRÃO PRETO","SANTO AMARO","SANTOS","SOROCABA","SÃO BERNARDO","TATUAPÉ","TIJUCA","TUCURUVI","VILA MASCOTE"]

# Here i wanna show the evolution of Sales Costs of Sales and serve, contribuition margin, ...

df_sales_path = "base_de_dados/sales/Sales_View/Cópia de data_sales_2024_updated.csv"
df_sales = pd.read_csv(df_sales_path)

df_sales = df_sales.loc[df_sales['CORTESIA'] != True]
groupby_for_sales = df_sales.groupby(["Unidade", "Mês venda", "Grupo"]).agg({"Valor liquido item": "sum","Quantidade" : "sum",
                                                                                      "Valor tabela item" : "sum", "Custo Direto" : "sum"}).reset_index()

# Evolution od Sales:

groupby_for_sales_evolution = groupby_for_sales.groupby(["Grupo", "Mês venda"]).agg({"Valor liquido item" : "sum"}).reset_index()
st.bar_chart(groupby_for_sales_evolution)

st.dataframe(groupby_for_sales_evolution)
