import streamlit as st

# --- PAGE SETUP ---
page_1 = st.Page(
    "views/sales_view.py",
    title="Análises",
    icon=":material/thumb_up:"
)

# --- PAGE SETUP ---
page_2 = st.Page(
    "views/appointments_view.py",
    title="Análises",
    icon=":material/thumb_up:",
    default=True,
)

# --- SUBPAGES SETUP FOR PAGE 1 ---
subpage_1_1 = st.Page(
    "views/Sales_categorys_view.py",
    title="Evolução Gráfica",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Visão - Vendas": [page_1,subpage_1_1],
        "Visão - Agendamento": [page_2],
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
