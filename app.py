import streamlit as st
import pandas as pd
import os

# Set up the Streamlit page
st.set_page_config(page_title="DashBoard Financeiro - Pró-Corpo Estética", page_icon="💎", layout="wide")

# Title of the Dashboard
st.title("DashBoard Financeiro - Pró-Corpo Estética")

# Sidebar navigation
st.sidebar.title("Análises - Pró-Corpo")
page = st.sidebar.radio("Ir Para", ["Visão - Vendas", "Visão - Agendamentos", "Indicadores Gerais"])

# Path to the sales indicators CSV file
df_sales_all_indicators_path = "base_de_dados/sales/all_indicators_sales.csv"
df_sales_average_price_path = "base_de_dados/sales/df_average_price.csv"
df_sales_contribution_margin_path = "base_de_dados/sales/df_contribution_margin.csv"
df_sales_main_products_path = "base_de_dados/sales/df_main_products.csv"
df_sales_quantity_sold_path = "base_de_dados/sales/df_quantity_sold.csv"

# Path to the appointments indicators CSV file
df_appointments_all_indicators_path = "base_de_dados/appointments/all_indicators_appointments.csv"
df_appointments_cortesy_analysis_path = "base_de_dados/appointments/courtesy_analysis.csv"
df_appointments_direct_costs_path = "base_de_dados/appointments/direct_costs.csv"
df_appointments_main_served_procedeures_path = "base_de_dados/appointments/main_served_procedeures.csv"
df_appointmentes_time_taken_from_schedule_path = "base_de_dados/appointments/time_taken_from_schedule.csv"



if page == "Visão - Vendas":

  st.subheader("Visão - Vendas")
  sales_option = st.selectbox("O que você quer ver de Vendas?", ["Todos Indicadores", "Preço Médio", "Margem de Contribuição","Produtos mais Vendidos", "Quantidade Vendida"])

  if sales_option == "Todos Indicadores":


    df_sales_all_indicators = pd.read_csv(df_sales_all_indicators_path)
    st.dataframe(df_sales_all_indicators)

  elif sales_option == "Preço Médio":
    df_sales_average_price = pd.read_csv(df_sales_average_price_path)
    st.dataframe(df_sales_average_price)

  elif sales_option == "Margem de Contribuição":
    df_sales_contribution_margin = pd.read_csv(df_sales_contribution_margin_path)
    st.dataframe(df_sales_contribution_margin)

  elif sales_option == "Produtos mais Vendidos":
    df_sales_main_products = pd.read_csv(df_sales_main_products_path)
    st.dataframe(df_sales_main_products)

  elif sales_option == "Quantidade Vendida":
    df_sales_quantity_sold = pd.read_csv(df_sales_quantity_sold_path)
    st.dataframe(df_sales_quantity_sold)

  else:
    st.write("Escolha uma opção válida.")

elif page == "Visão - Agendamentos":
  st.subheader("Visão - Agendamentos")
  appointments_option = st.selectbox("O que você quer ver de Agendamentos?", ["Todos Indicadores", "Procedimentos mais atendidos", "Tempo de Agenda", "Custos Diretos", "Análise de Cortesia"])

  if appointments_option == "Todos Indicadores":
    df_appointments_all_indicators = pd.read_csv(df_appointments_all_indicators_path)
    st.dataframe(df_appointments_all_indicators)

  elif appointments_option == "Procedimentos mais atendidos":
    df_appointments_main_served_procedeures = pd.read_csv(df_appointments_main_served_procedeures_path)
    st.dataframe(df_appointments_main_served_procedeures)

  elif appointments_option == "Tempo de Agenda":
    df_appointmentes_time_taken_from_schedule = pd.read_csv(df_appointmentes_time_taken_from_schedule_path)
    st.dataframe(df_appointmentes_time_taken_from_schedule)

  elif appointments_option == "Custos Diretos":
    df_appointments_direct_costs = pd.read_csv(df_appointments_direct_costs_path)
    st.dataframe(df_appointments_direct_costs)

  elif appointments_option == "Análise de Cortesia":
    df_appointments_cortesy_analysis = pd.read_csv(df_appointments_cortesy_analysis_path)
    st.dataframe(df_appointments_cortesy_analysis)

  else:
    st.write("Escolha uma opção válida.")

else:
  st.subheader("Indicadores Gerais")
