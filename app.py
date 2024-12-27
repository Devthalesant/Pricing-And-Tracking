import streamlit as st

# --- PAGE SETUP ---
page_1 = st.Page(
    "views/general_view.py",
    title="Análises",
    icon=":material/thumb_up:"
)



# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Visão - Vendas": [page_1]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
