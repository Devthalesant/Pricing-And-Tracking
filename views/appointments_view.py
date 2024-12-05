import streamlit as st
import pandas as pd


Month_list = ["Anual","Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
branch_list = ["TODAS","ALPHAVILLE","BELO HORIZONTE","CAMPINAS","COPACABANA","IPIRANGA","ITAIM","JARDINS","LAPA","LONDRINA","MOEMA","MOOCA","OSASCO",
               "RIBEIRÃO PRETO","SANTO AMARO","SANTOS","SOROCABA","SÃO BERNARDO","TATUAPÉ","TIJUCA","TUCURUVI","VILA MASCOTE"]
appointments_option = ["Custo e Tempo Total", "Custos Diretos", "Mais Atendidos","Tempo de Agenda", "Análise de Cortesia"]

# Path to the appointments indicators CSV file
df_appointments_total_time_and_cost_path = "base_de_dados/appointments/Appointments_View/total_time_and_cost.csv"
df_appointments_cortesy_analysis_path = "base_de_dados/appointments/Appointments_View/courtesy_analysis.csv"
df_appointments_direct_costs_path = "base_de_dados/appointments/Appointments_View/direct_costs.csv"
df_appointments_main_served_procedeures_path = "base_de_dados/appointments/Appointments_View/main_served_procedeures.csv"
df_appointmentes_time_taken_from_schedule_path = "base_de_dados/appointments/Appointments_View/time_taken_from_schedule.csv"

st.subheader("Visão - Agendamentos 💎")

appointments_option = st.selectbox("O que você quer ver de Agendamentos?", appointments_option)

col_1, col_2 = st.columns(2)

with col_1:
    month_selector = st.multiselect("Escolha o mês", Month_list)
with col_2:
    branch_selector = st.multiselect("Escolha a Unidade do agendamento", branch_list)


if appointments_option == "Custo e Tempo Total":
  df_appointments_total_time_and_cost_path = pd.read_csv(df_appointments_total_time_and_cost_path)


  if len(month_selector) == 0 and len(branch_selector) == 0:
    df_appointments_total_time_and_cost_path = df_appointments_total_time_and_cost_path
    st.dataframe(df_appointments_total_time_and_cost_path)

  elif "Anual" in month_selector and "TODAS" in branch_selector:
      st.dataframe(df_appointments_total_time_and_cost_path)

  elif "Anual" in month_selector and "TODAS" not in branch_selector:
      df_appointments_total_time_and_cost_path = df_appointments_total_time_and_cost_path.loc[df_appointments_total_time_and_cost_path['Unidade do agendamento'].isin(branch_selector)]
      st.dataframe(df_appointments_total_time_and_cost_path)

  elif "Anual" not in month_selector and "TODAS" in branch_selector:
      df_appointments_total_time_and_cost_path = df_appointments_total_time_and_cost_path.loc[df_appointments_total_time_and_cost_path['Mês Atendimento'].isin(month_selector)]
      st.dataframe(df_appointments_total_time_and_cost_path)

  elif "Anual" not in month_selector and "TODAS" not in branch_selector:
      df_appointments_total_time_and_cost_path = df_appointments_total_time_and_cost_path.loc[df_appointments_total_time_and_cost_path['Mês Atendimento'].isin(month_selector) &
                                                                                        df_appointments_total_time_and_cost_path['Unidade do agendamento'].isin(branch_selector)]
      st.dataframe(df_appointments_total_time_and_cost_path)

elif appointments_option == "Custos Diretos":
  df_appointments_direct_costs = pd.read_csv(df_appointments_direct_costs_path)

  if len(month_selector) == 0 and len(branch_selector) == 0:
    df_appointments_direct_costs = df_appointments_direct_costs
    st.dataframe(df_appointments_direct_costs)

  elif "Anual" in month_selector and "TODAS" in branch_selector:
      st.dataframe(df_appointments_direct_costs)

  elif "Anual" in month_selector and "TODAS" not in branch_selector:
      df_appointments_direct_costs = df_appointments_direct_costs.loc[df_appointments_direct_costs['Unidade do agendamento'].isin(branch_selector)]
      st.dataframe(df_appointments_direct_costs)

  elif "Anual" not in month_selector and "TODAS" in branch_selector:
      df_appointments_direct_costs = df_appointments_direct_costs.loc[df_appointments_direct_costs['Mês Atendimento'].isin(month_selector)]
      st.dataframe(df_appointments_direct_costs)

  elif "Anual" not in month_selector and "TODAS" not in branch_selector:
      df_appointments_direct_costs = df_appointments_direct_costs.loc[df_appointments_direct_costs['Mês Atendimento'].isin(month_selector) &
                                                          df_appointments_direct_costs['Unidade do agendamento'].isin(branch_selector)]
      st.dataframe(df_appointments_direct_costs)

elif appointments_option == "Mais Atendidos":
  df_appointments_main_served_procedeures = pd.read_csv(df_appointments_main_served_procedeures_path)

  if len(month_selector) == 0 and len(branch_selector) == 0:
    df_appointments_main_served_procedeures = df_appointments_main_served_procedeures
    st.dataframe(df_appointments_main_served_procedeures)

  elif "Anual" in month_selector and "TODAS" in branch_selector:
      st.dataframe(df_appointments_main_served_procedeures)

  elif "Anual" in month_selector and "TODAS" not in branch_selector:
      df_appointments_main_served_procedeures = df_appointments_main_served_procedeures.loc[df_appointments_main_served_procedeures['Unidade do agendamento'].isin(branch_selector)]
      st.dataframe(df_appointments_main_served_procedeures)

  elif "Anual" not in month_selector and "TODAS" in branch_selector:
      df_appointments_main_served_procedeures = df_appointments_main_served_procedeures.loc[df_appointments_main_served_procedeures['Mês Atendimento'].isin(month_selector)]
      st.dataframe(df_appointments_main_served_procedeures)

  elif "Anual" not in month_selector and "TODAS" not in branch_selector:
      df_appointments_main_served_procedeures = df_appointments_main_served_procedeures.loc[df_appointments_main_served_procedeures['Mês Atendimento'].isin(month_selector) &
                                                                      df_appointments_main_served_procedeures['Unidade do agendamento'].isin(branch_selector)]
      st.dataframe(df_appointments_main_served_procedeures)

elif appointments_option == "Tempo de Agenda":
  df_appointmentes_time_taken_from_schedule = pd.read_csv(df_appointmentes_time_taken_from_schedule_path)

  if len(month_selector) == 0 and len(branch_selector) == 0:
    df_appointmentes_time_taken_from_schedule = df_appointmentes_time_taken_from_schedule
    st.dataframe(df_appointmentes_time_taken_from_schedule)

  elif "Anual" in month_selector and "TODAS" in branch_selector:
      st.dataframe(df_appointmentes_time_taken_from_schedule)

  elif "Anual" in month_selector and "TODAS" not in branch_selector:
      df_appointmentes_time_taken_from_schedule = df_appointmentes_time_taken_from_schedule.loc[df_appointmentes_time_taken_from_schedule['Unidade do agendamento'].isin(branch_selector)]
      st.dataframe(df_appointmentes_time_taken_from_schedule)

  elif "Anual" not in month_selector and "TODAS" in branch_selector:
      df_appointmentes_time_taken_from_schedule = df_appointmentes_time_taken_from_schedule.loc[df_appointmentes_time_taken_from_schedule['Mês Atendimento'].isin(month_selector)]
      st.dataframe(df_appointmentes_time_taken_from_schedule)

  elif "Anual" not in month_selector and "TODAS" not in branch_selector:
      df_appointmentes_time_taken_from_schedule = df_appointmentes_time_taken_from_schedule.loc[df_appointmentes_time_taken_from_schedule['Mês Atendimento'].isin(month_selector) &
                                                          df_appointmentes_time_taken_from_schedule['Unidade do agendamento'].isin(branch_selector)]
      st.dataframe(df_appointmentes_time_taken_from_schedule)

elif appointments_option == "Análise de Cortesia":
  df_appointments_cortesy_analysis = pd.read_csv(df_appointments_cortesy_analysis_path)

  if len(month_selector) == 0 and len(branch_selector) == 0:
    df_appointments_cortesy_analysis = df_appointments_cortesy_analysis
    st.dataframe(df_appointments_cortesy_analysis)

  elif "Anual" in month_selector and "TODAS" in branch_selector:
      st.dataframe(df_appointments_cortesy_analysis)

  elif "Anual" in month_selector and "TODAS" not in branch_selector:
      df_appointments_cortesy_analysis = df_appointments_cortesy_analysis.loc[df_appointments_cortesy_analysis['Unidade do agendamento'].isin(branch_selector)]
      st.dataframe(df_appointments_cortesy_analysis)

  elif "Anual" not in month_selector and "TODAS" in branch_selector:
      df_appointments_cortesy_analysis = df_appointments_cortesy_analysis.loc[df_appointments_cortesy_analysis['Mês Atendimento'].isin(month_selector)]
      st.dataframe(df_appointments_cortesy_analysis)

  elif "Anual" not in month_selector and "TODAS" not in branch_selector:
      df_appointments_cortesy_analysis = df_appointments_cortesy_analysis.loc[df_appointments_cortesy_analysis['Mês Atendimento'].isin(month_selector) &
                                                          df_appointments_cortesy_analysis['Unidade do agendamento'].isin(branch_selector)]
      st.dataframe(df_appointments_cortesy_analysis)

else:
  st.write("Escolha uma opção válida.")
