import streamlit as st
import pandas as pd

st.set_page_config(page_title="DashBoard Financeiro - Pró-Corpo Estética", page_icon="💎", layout="wide")

st.title("DashBoard Financeiro - Pró-Corpo Estética")

st.sidebar.title("Análises - Pró-Corpo")
page = st.sidebar.radio("Go to", ["Iníco", "Visão - Vendas", "Visão - Agendamentos", "Indicadores Gerais"])
