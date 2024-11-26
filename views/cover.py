import streamlit as st
import pandas as pd

# Set up the Streamlit page
st.set_page_config(page_title="DashBoard Financeiro - Pró-Corpo Estética", page_icon="💎", layout="wide")

# Title of the Dashboard
st.title("DashBoard Financeiro - Pró-Corpo Estética")

# Sidebar navigation
st.sidebar.title("Análises - Pró-Corpo")
page = st.sidebar.radio("Go to", ["Visão - Vendas", "Visão - Agendamentos", "Indicadores Gerais"])

# Path to the sales indicators CSV file
df_sales_path_all_indicators = "/content/Pricing-And-Tracking/base_de_dados/all_indicators_sales.csv"

if page == "Visão - Vendas":
    # Load the sales indicators DataFrame
    try:
        df_sales_all_indicators = pd.read_csv(df_sales_path_all_indicators)
        st.dataframe(df_sales_all_indicators)  # Display the DataFrame
    except FileNotFoundError:
        st.error("Sales data file not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        st.error("Sales data file is empty.")
    except pd.errors.ParserError:
        st.error("Error parsing the sales data file. Please check the file format.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    st.write("Página não encontrada.")
