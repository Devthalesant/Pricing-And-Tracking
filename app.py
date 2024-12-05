import streamlit as st

# --- PAGE SETUP ---
# Páginas principais
page_1 = st.Page(
    "views/sales_view.py",
    title="Visão - Vendas",
    icon=":material/thumb_up:"
)

page_2 = st.Page(
    "views/appointments_view.py",
    title="Visão - Agendamento",
    icon=":material/home:",
    default=True,
)

# --- SUBPAGES SETUP FOR PAGE 1 ---
subpage_1_1 = st.Page(
    "views/sales_subpage_1.py",
    title="Subpágina 1.1",
)
subpage_1_2 = st.Page(
    "views/sales_subpage_2.py",
    title="Subpágina 1.2",
)

# --- SUBPAGES SETUP FOR PAGE 2 ---
subpage_2_1 = st.Page(
    "views/appointments_subpage_1.py",
    title="Subpágina 2.1",
)
subpage_2_2 = st.Page(
    "views/appointments_subpage_2.py",
    title="Subpágina 2.2",
)

# --- NAVIGATION SETUP ---
pg = st.navigation(
    {
        "Pages": [page_1, page_2],
        "Subpáginas - Vendas": [subpage_1_1, subpage_1_2],
        "Subpáginas - Agendamento": [subpage_2_1, subpage_2_2],
    }
)

# --- RUN NAVIGATION ---
pg.run()
