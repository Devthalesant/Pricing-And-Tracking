import streamlit as st
import pandas as pd

# Set up the Streamlit page
st.set_page_config(page_title="DashBoard Financeiro - Pró-Corpo Estética", page_icon="💎", layout="wide")

# Title of the Dashboard
st.title("DashBoard Financeiro - Pró-Corpo Estética")

# Sidebar navigation
st.sidebar.title("Análises - Pró-Corpo")
page = st.sidebar.radio("Go to", ["Início", "Visão - Vendas", "Visão - Agendamentos", "Indicadores Gerais"])

# Image path for the logo
image_path = "/content/Pricing-And-Tracking/views/logo_vertical.png "

# Display the image
st.image(image_path, caption="Logo", use_column_width=True)
