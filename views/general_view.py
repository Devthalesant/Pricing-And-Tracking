from pymongo import MongoClient, UpdateOne
from auxiliar.catching_and_treating_values_functions import *
from auxiliar.groupby import *
import streamlit as st
import pandas as pd
import re

st.title("Visão Geral - Perído TESTE")
# Getting a dataframe of billchaeges
billcharges_df = get_dataframe_from_mongodb(collection_name="billcharges_db", database_name="dash_midia")

new_df = treating_values(billcharges_df)
var = grafico_barras_vendas(new_df)

st.dataframe(var)
st.dataframe(new_df)
st.dash_midiaataFrame(billcharges_df)

teste = new_df['STATUS'].unique()

st.write(teste)
