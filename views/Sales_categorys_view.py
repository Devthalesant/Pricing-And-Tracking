import streamlit as st
import pandas as pd


Month_list = ["Anual","Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
branch_list = ["TODAS","ALPHAVILLE","BELO HORIZONTE","CAMPINAS","COPACABANA","IPIRANGA","ITAIM","JARDINS","LAPA","LONDRINA","MOEMA","MOOCA","OSASCO",
               "RIBEIRÃO PRETO","SANTO AMARO","SANTOS","SOROCABA","SÃO BERNARDO","TATUAPÉ","TIJUCA","TUCURUVI","VILA MASCOTE"]
months_order = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
               'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Here i wanna show the evolution of Sales Costs of Sales and serve, contribuition margin, ...

st.title("Visão - Vendas 💎")
df_sales_path = "base_de_dados/sales/Sales_View/Cópia de data_sales_2024_updated.csv"
df_sales = pd.read_csv(df_sales_path)

df_sales = df_sales.loc[df_sales['CORTESIA'] != True]
groupby_for_sales = df_sales.groupby(["Unidade", "Mês venda", "Grupo"]).agg({"Valor liquido item": "sum","Quantidade" : "sum",
                                                                                      "Valor tabela item" : "sum", "Custo Direto" : "sum"}).reset_index()

groupby_for_sales_evolution = groupby_for_sales.groupby(["Grupo", "Mês venda"]).agg({"Valor liquido item" : "sum"}).reset_index()

# Evolution Sales

  #General

General_sales = groupby_for_sales_evolution

General_sales['Mês venda'] = pd.Categorical(General_sales['Mês venda'], categories= months_order, ordered=True)
General_sales = General_sales.sort_values(by="Mês venda")

st.subheader("Gráfico de Evolução de Vendas - Geral")
st.bar_chart(General_sales, x="Mês venda", y="Valor liquido item",color =(160, 32, 240, 1.0))

  #Medicina Estética

sales_evolution_med = groupby_for_sales_evolution.loc[groupby_for_sales_evolution['Grupo'] == "MEDICINA ESTÉTICA"]

sales_evolution_med['Mês venda'] = pd.Categorical(sales_evolution_med['Mês venda'], categories= months_order, ordered=True)
sales_evolution_med = sales_evolution_med.sort_values(by="Mês venda")

st.subheader("Gráfico de Evolução de Vendas - Medicina Estética")
st.bar_chart(sales_evolution_med, x="Mês venda", y="Valor liquido item",color =(160, 32, 240, 1.0))

  #ESTÉTICA

sales_evolution_est = groupby_for_sales_evolution.loc[groupby_for_sales_evolution['Grupo'] == "ESTÉTICA"]

sales_evolution_est['Mês venda'] = pd.Categorical(sales_evolution_est['Mês venda'], categories= months_order, ordered=True)
sales_evolution_est = sales_evolution_est.sort_values(by="Mês venda")

st.subheader("Gráfico de Evolução de Vendas - Estética")
st.bar_chart(sales_evolution_est, x="Mês venda", y="Valor liquido item",color =(160, 32, 240, 1.0))

  #ULTRAFORMER_III

sales_evolution_ultra = groupby_for_sales_evolution.loc[groupby_for_sales_evolution['Grupo'] == "ULTRAFORMER_III"]

sales_evolution_ultra['Mês venda'] = pd.Categorical(sales_evolution_ultra['Mês venda'], categories= months_order, ordered=True)
sales_evolution_ultra = sales_evolution_ultra.sort_values(by="Mês venda")

st.subheader("Gráfico de Evolução de Vendas - Ultraformer III")
st.bar_chart(sales_evolution_ultra, x="Mês venda", y="Valor liquido item",color =(160, 32, 240, 1.0))

  #LAVIEEN

sales_evolution_lavieen = groupby_for_sales_evolution.loc[groupby_for_sales_evolution['Grupo'] == "LAVIEEN"]

sales_evolution_lavieen['Mês venda'] = pd.Categorical(sales_evolution_lavieen['Mês venda'], categories= months_order, ordered=True)
sales_evolution_lavieen = sales_evolution_lavieen.sort_values(by="Mês venda")

st.subheader("Gráfico de Evolução de Vendas - Lavieen")
st.bar_chart(sales_evolution_lavieen, x="Mês venda", y="Valor liquido item",color =(160, 32, 240, 1.0))
