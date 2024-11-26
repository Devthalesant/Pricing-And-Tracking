import streamlit as st
import pandas as pd


# Set up the Streamlit page
st.set_page_config(page_title="DashBoard Financeiro - Pró-Corpo Estética", page_icon="💎", layout="wide")

# Title of the Dashboard
st.title("DashBoard Financeiro - Pró-Corpo Estética")

# Sidebar navigation
st.sidebar.title("Análises - Pró-Corpo")
page = st.sidebar.radio("Go to", ["Visão - Vendas", "Visão - Agendamentos", "Indicadores Gerais"])

# Image path for the logo
image_path = "/content/Pricing-And-Tracking/logo_vertical.png"

# Path to All_indicators_sales: 
df_sales_path_all_indicators = "/content/Pricing-And-Tracking/base_de_dados/all_indicators_sales.csv"
df_sales_all_indicators = pd.read_csv(df_sales_all_indicators)

# Display the image
st.image(image_path, caption="Logo", use_column_width=True)

if page == "Visão - Vendas":
    # Content for the "Visão - Vendas" page
    st.header("Visão - Vendas")
    st.dataframe(df_sales_all_indicators)

# elif page == "Visão - Agendamentos":
#     # Content for the "Visão - Agendamentos" page
#     st.header("Visão - Agendamentos")
#     st.dataframe(df_appointmnents)
