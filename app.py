import streamlit as st

# --- PAGE SETUP ---
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
    "views/Sales_categorys_view.py",
    title="Evolução Gráfica - Vendas",
)

subpage_1_2 = st.Page(
    "views/Sales_another_view.py",  # Adicione outra subpágina conforme necessário
    title="Outra Subpágina - Vendas",
)

# --- SUBPAGES SETUP FOR PAGE 2 ---
subpage_2_1 = st.Page(
    "views/Appointments_details_view.py",  # Exemplo de subpágina para Agendamento
    title="Detalhes do Agendamento",
)

subpage_2_2 = st.Page(
    "views/Appointments_statistics_view.py",  # Outra subpágina para Agendamento
    title="Estatísticas do Agendamento",
)

# --- NAVIGATION SETUP ---
pg = st.navigation(
    {
        "Visão - Vendas": [page_1, subpage_1_1, subpage_1_2],
        "Visão - Agendamento": [page_2, subpage_2_1, subpage_2_2],
    }
)

# --- RUN NAVIGATION ---
pg.run()
