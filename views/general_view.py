from auxiliar.catching_and_treating_values_functions import *
import streamlit as st
import pandas as pd


collection_name="billcharges_db"
database_name="dash_midia"

# Chame a função que trata os valores. Certifique-se de que essa função retorna ou manipula new_df de forma correta.
get_dataframe_from_mongodb(collection_name, database_name, query={})
new_df = treating_values()  # Supondo que treating_values retorna um DataFrame

# Exibe o DataFrame no Streamlit
st.dataframe(new_df)
