import streamlit as st
import pandas as pd
import os
import random
from Pricing&Tracking.ipynb import treating_values

treating_values()

st.dataframe(new_df)
