from auxiliar.catching_and_treating_values_functions import *
import streamlit as st

# Obtendo um dataframe de billcharges
billcharges_df = get_dataframe_from_mongodb(collection_name="billcharges_db", database_name="dash_midia")

# Chame a função que trata os valores
new_df = treating_values(billcharges_df)

# Exibe o DataFrame no Streamlit
st.title("Dados Tratados")
st.dataframe(new_df)
