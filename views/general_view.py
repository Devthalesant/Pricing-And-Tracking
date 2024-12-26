from auxiliar.auxiliar import *
import streamlit as st
import pandas as pd

# Chame a função que trata os valores. Certifique-se de que essa função retorna ou manipula new_df de forma correta.
get_dataframe_from_mongodb(collection_name, database_name, query={})
extract_quote_items(row)
new_df = treating_values()  # Supondo que treating_values retorna um DataFrame

# Exibe o DataFrame no Streamlit
st.dataframe(new_df)
