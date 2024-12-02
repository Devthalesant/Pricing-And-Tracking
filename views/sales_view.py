import streamlit as st
import pandas as pd
import os
import random
from auxiliar.aux_sales_view import *

Month_list = ["janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

#Path to the sales indicators CSV file
df_sales_all_indicators_path = "base_de_dados/sales/Sales_View/all_indicators_sales.csv"
df_sales_average_price_path = "base_de_dados/sales/Sales_View/df_average_price.csv"
df_sales_contribution_margin_path = "base_de_dados/sales/Sales_View/df_contribution_margin.csv"
df_sales_main_products_path = "base_de_dados/sales/Sales_View/df_main_products.csv"
df_sales_quantity_sold_path = "base_de_dados/sales/Sales_View/df_quantity_sold.csv"

st.subheader("Visão - Vendas")
sales_option = st.selectbox("O que você quer ver de Vendas?", ["Todos Indicadores", "Preço Médio", "Margem de Contribuição","Produtos mais Vendidos", "Quantidade Vendida"])
month_selector = st.selectbox("Escolha o mês", Month_list)


if sales_option == "Todos Indicadores":
  df_sales_all_indicators = pd.read_csv(df_sales_all_indicators_path)
  df_sales_all_indicators = df_sales_all_indicators.loc[df_sales_all_indicators['Mês venda'].isin(month_selector)]
  st.dataframe(df_sales_all_indicators)

elif sales_option == "Preço Médio":
  df_sales_average_price = pd.read_csv(df_sales_average_price_path)
  df_sales_average_price = df_sales_average_price.loc[df_sales_average_price['Mês venda'].isin(month_selector)]
  st.dataframe(df_sales_average_price)

elif sales_option == "Margem de Contribuição":
  df_sales_contribution_margin = pd.read_csv(df_sales_contribution_margin_path)
  df_sales_contribution_margin = df_sales_contribution_margin.loc[df_sales_contribution_margin['Mês venda'].isin(month_selector)]
  st.dataframe(df_sales_contribution_margin)

elif sales_option == "Produtos mais Vendidos":
  df_sales_main_products = pd.read_csv(df_sales_main_products_path)
  df_sales_main_products = df_sales_main_products.loc[df_sales_main_products['Mês venda'].isin(month_selector)]
  st.dataframe(df_sales_main_products)

elif sales_option == "Quantidade Vendida":
  df_sales_quantity_sold = pd.read_csv(df_sales_quantity_sold_path)
  df_sales_quantity_sold = df_sales_quantity_sold.loc[df_sales_quantity_sold['Mês venda'].isin(month_selector)]
  st.dataframe(df_sales_quantity_sold)

else:
  st.write("Escolha uma opção válida.")
