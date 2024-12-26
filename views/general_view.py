import streamlit as st
import pandas as pd
import os
import random
from Pricing_and_Tracking.py import treating_values

treating_values()

st.dataframe(new_df)
