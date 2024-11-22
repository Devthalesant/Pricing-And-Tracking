import streamlit as st
import pandas as pd

st.set_page_config(page_title="Teste DataFrame", page_icon="💎", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/ALL/data_sales_2024_updated_try.csv")

df_sales = load_data()

st.title("Meu novo dataframe")

st.dataframe(df_sales)
