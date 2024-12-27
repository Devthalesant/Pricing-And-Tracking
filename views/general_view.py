from pymongo import MongoClient, UpdateOne
from auxiliar.catching_and_treating_values_functions import *
from auxiliar.groupby import *
import streamlit as st
import pandas as pd
import re

st.title("Visão Geral - Perído ARROBA")
# Getting a dataframe of billchaeges
billcharges_df = get_dataframe_from_mongodb(collection_name="billcharges_db", database_name="dash_midia")

new_df = treating_values(billcharges_df)
grafico = grafico_barras_vendas(new_df)

st.plotly_chart(grafico, use_container_width=True)
