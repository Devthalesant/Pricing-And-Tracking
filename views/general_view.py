import streamlit as st
import pandas as pd
import os
import random
from Pricing_and_Tracking import treating_values

# Chame a função que trata os valores. Certifique-se de que essa função retorna ou manipula new_df de forma correta.
new_df = treating_values()  # Supondo que treating_values retorna um DataFrame

# Exibe o DataFrame no Streamlit
st.dataframe(new_df)
