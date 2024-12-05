import streamlit as st

# --- PAGE SETUP ---
page_1 = st.Page(
    "views/sales_view.py",
    title="Visão - Vendas",
    icon=":material/thumb_up:"
)

# --- PAGE SETUP ---
page_2 = st.Page(
    "views/appointments_view.py",
    title="VIsão - Agendamento",
    icon=":material/home:",
    default=True,
)

# --- SUBPAGES SETUP FOR PAGE 1 ---
subpage_1_1 = st.Page(
    "views/Sales_categorys_view.py",
    title="Evolução Gráfica - Vendas",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Pages": [page_1,page_2],
        "Visão - Vendas": [subpage_1_1],
        "Visão - Agendamento": [],
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
