from pymongo import MongoClient, UpdateOne
from auxiliar.catching_and_treating_values_functions import *
import streamlit as st
import pandas as pd

# Getting a dataframe of billchaeges
billcharges_df = get_dataframe_from_mongodb(collection_name="billcharges_db", database_name="dash_midia")
# Dropping dulicates from quote_ID because there is all i need in quote_items:
billcharges_df.drop_duplicates(subset=['quote_id'],keep='first', inplace=True)

new_df = treating_values()
# Exibe o DataFrame no Streamlit
st.dataframe(new_df)
