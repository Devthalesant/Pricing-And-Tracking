import streamlit as st
import pandas as pd
import os
import random
from auxiliar.aux_sales_view import *

df_sales_all_indicators, df_sales_average_price, df_sales_contribution_margin, df_sales_main_products, df_sales_quantity_sold = sales_view()

# Path to the sales indicators CSV file
# df_sales_all_indicators_path = "base_de_dados/sales/all_indicators_sales.csv"
# df_sales_average_price_path = "base_de_dados/sales/df_average_price.csv"
# df_sales_contribution_margin_path = "base_de_dados/sales/df_contribution_margin.csv"
# df_sales_main_products_path = "base_de_dados/sales/df_main_products.csv"
# df_sales_quantity_sold_path = "base_de_dados/sales/df_quantity_sold.csv"

st.subheader("Visão - Vendas")
sales_option = st.selectbox("O que você quer ver de Vendas?", ["Todos Indicadores", "Preço Médio", "Margem de Contribuição","Produtos mais Vendidos", "Quantidade Vendida"])

if sales_option == "Todos Indicadores":
  # df_sales_all_indicators = pd.read_csv(df_sales_all_indicators_path)
  st.dataframe(df_sales_all_indicators)

elif sales_option == "Preço Médio":
  # df_sales_average_price = pd.read_csv(df_sales_average_price_path)
  st.dataframe(df_sales_average_price)

elif sales_option == "Margem de Contribuição":
  # df_sales_contribution_margin = pd.read_csv(df_sales_contribution_margin_path)
  st.dataframe(df_sales_contribution_margin)

elif sales_option == "Produtos mais Vendidos":
  # df_sales_main_products = pd.read_csv(df_sales_main_products_path)
  st.dataframe(df_sales_main_products)

elif sales_option == "Quantidade Vendida":
  # df_sales_quantity_sold = pd.read_csv(df_sales_quantity_sold_path)
  st.dataframe(df_sales_quantity_sold)

else:
  st.write("Escolha uma opção válida.")
