import streamlit as st
import pandas as pd

# Set up the Streamlit page
st.set_page_config(page_title="DashBoard Financeiro - Pró-Corpo Estética", page_icon="💎", layout="wide")

# Title of the Dashboard
st.title("DashBoard Financeiro - Pró-Corpo Estética")

# Sidebar navigation
st.sidebar.title("Análises - Pró-Corpo")
page = st.sidebar.radio("Ir Para", ["Visão - Vendas", "Visão - Agendamentos", "Indicadores Gerais"])

# Path to the sales indicators CSV file
# df_sales_path_all_indicators = "/content/Pricing-And-Tracking/base_de_dados/all_indicators_sales.csv"

if page == "Visão - Vendas":

  st.subheader("Visão - Vendas")
  sales_option = st.selectbox("O que você quer ver de Vendas?", ["Todos Indicadores", "Preço Médio", "Margem de Contribuição","Produtos mais Vendidos", "Quantidade Vendida"])
  
  if sales_option == "Todos Indicadores":

    df_sales_all_indicators = pd.read_csv("/content/Pricing-And-Tracking/base_de_dados/all_indicators_sales.csv")
    st.dataframe(df_sales_all_indicators)
  
  if sales_option == "Preço Médio":
    df_sales_average_price = pd.read_csv("/content/Pricing-And-Tracking/base_de_dados/df_average_price.csv")
    st.dataframe(df_sales_average_price)

  if sales_option == "Margem de Contribuição":
    df_sales_contribution_margin = pd.read_csv("/content/Pricing-And-Tracking/base_de_dados/df_contribution_margin.csv")
    st.dataframe(df_sales_contribution_margin)

  if sales_option == "Produtos mais Vendidos":
    df_sales_main_products = pd.read_csv("/content/Pricing-And-Tracking/base_de_dados/df_main_products.csv")
    st.dataframe(df_sales_main_products)
  
  if sales_option == "Quantidade Vendida":
    df_sales_quantity_sold = pd.read_csv("/content/Pricing-And-Tracking/base_de_dados/df_quantity_sold.csv")
    st.dataframe(df_sales_quantity_sold)
  
  else: 
    st.write("Escolha uma opção válida.")

else: 
  st.subheader("Visão - Agendamentos")
  
