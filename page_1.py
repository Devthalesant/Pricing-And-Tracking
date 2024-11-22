import streamlit as st
import pandas as pd
import datetime
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Teste DataFrame", page_icon="💎",layout="wide")

@st.cache_data

df_sales = pd.read_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/ALL/data_sales_2024_updated_try.csv")


st.title("Meu novo dataframe")

st.dataframe(df_sales)
