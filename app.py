import streamlit as st
import pandas as pd

# --- PAGE SETUP ---
cover_page = st.Page(
    "views/cover.py",
    title="Cover",
    default=True,
)

sales_page = st.Page(
    "views/sales_view.py",
    title="Sales View",
    default=True,
)

appointments_page = st.Page(
    "views/appointments_view.py",
    title="Appointments View",
    default=True,
)

merged_page = st.Page(
    "views/merged_view.py",
    title="Merged View",
    default=True,
)

# --- NAVIGATION SETUP WITH SECTIONS ---
pg = st.navigation(
    {
        "Cover": [cover_page],
        "Sales": [sales_page],
        "Appointments": [appointments_page],
        "Merged": [merged_page]
    }
)

# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")

# --- RUN NAVIGATION ---
pg.run()
