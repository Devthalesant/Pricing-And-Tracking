import streamlit as st
import pandas as pd
import os


Month_list = ["janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

# Set up the Streamlit page
st.set_page_config(page_title="DashBoard Financeiro - Pró-Corpo Estética", page_icon="💎", layout="wide")

# Title of the Dashboard
st.title("DashBoard Financeiro - Pró-Corpo Estética")


# Path to the appointments indicators CSV file
df_appointments_all_indicators_path = "base_de_dados/appointments/Appointments_View/all_indicators_appointments.csv"
df_appointments_cortesy_analysis_path = "base_de_dados/appointments/Appointments_View/courtesy_analysis.csv"
df_appointments_direct_costs_path = "base_de_dados/appointments/Appointments_View/courtesy_analysis.csv"
df_appointments_main_served_procedeures_path = "base_de_dados/appointments/Appointments_View/main_served_procedeures.csv"
df_appointmentes_time_taken_from_schedule_path = "base_de_dados/appointments/Appointments_View/time_taken_from_schedule.csv"

st.subheader("Visão - Agendamentos")
appointments_option = st.selectbox("O que você quer ver de Agendamentos?", ["Todos Indicadores", "Procedimentos mais atendidos", "Tempo de Agenda", "Custos Diretos", "Análise de Cortesia"])
month_selector = st.selectbox("Escolha o mês", Month_list)


if appointments_option == "Todos Indicadores":
  df_appointments_all_indicators = pd.read_csv(df_appointments_all_indicators_path)
  df_appointments_all_indicators = df_appointments_all_indicators.loc[df_appointments_all_indicators['Mês Atendimento'].isin([month_selector])]
  st.dataframe(df_appointments_all_indicators)

elif appointments_option == "Procedimentos mais atendidos":
  df_appointments_main_served_procedeures = pd.read_csv(df_appointments_main_served_procedeures_path)
  df_appointments_main_served_procedeures = df_appointments_main_served_procedeures.loc[df_appointments_main_served_procedeures['Mês Atendimento'].isin([month_selector])]
  st.dataframe(df_appointments_main_served_procedeures)

elif appointments_option == "Tempo de Agenda":
  df_appointmentes_time_taken_from_schedule = pd.read_csv(df_appointmentes_time_taken_from_schedule_path)
  df_appointmentes_time_taken_from_schedule = df_appointmentes_time_taken_from_schedule.loc[df_appointmentes_time_taken_from_schedule['Mês Atendimento'].isin([month_selector])]
  st.dataframe(df_appointmentes_time_taken_from_schedule)

elif appointments_option == "Custos Diretos":
  df_appointments_direct_costs = pd.read_csv(df_appointments_direct_costs_path)
  df_appointments_direct_costs = df_appointments_direct_costs.loc[df_appointments_direct_costs['Mês Atendimento'].isin([month_selector])]
  st.dataframe(df_appointments_direct_costs)

elif appointments_option == "Análise de Cortesia":
  df_appointments_cortesy_analysis = pd.read_csv(df_appointments_cortesy_analysis_path)
  df_appointments_cortesy_analysis = df_appointments_cortesy_analysis.loc[df_appointments_cortesy_analysis['Mês Atendimento'].isin([month_selector])]
  st.dataframe(df_appointments_cortesy_analysis)

else:
  st.write("Escolha uma opção válida.")
