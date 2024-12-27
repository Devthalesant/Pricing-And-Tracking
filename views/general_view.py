from pymongo import MongoClient, UpdateOne
from auxiliar.catching_and_treating_values_functions import *
import streamlit as st
import pandas as pd
import re

# Getting a dataframe of billchaeges
billcharges_df = get_dataframe_from_mongodb(collection_name="billcharges_db", database_name="dash_midia")

# new_df = treating_values(billcharges_df)
st.dataframe(billcharges_df)
