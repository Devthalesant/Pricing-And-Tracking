
def appointments_view():
  Month_list = ["janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro"]
  branches_list = ['ALPHAVILLE','BELO HORIZONTE','CAMPINAS','COPACABANA','IPIRANGA','ITAIM','JARDINS','LAPA','LONDRINA','MOEMA','MOOCA','OSASCO','RIBEIRÃO PRETO','SANTO AMARO','SANTOS','SOROCABA','SÃO BERNARDO','TATUAPÉ','TIJUCA','TUCURUVI','VILA MASCOTE']

  # DF appointments Concatenated Paths
  df_appointments_view_path = "/content/drive/MyDrive/python - Thales/P&T/Bases CSV/ALL/data_appointments_2024_updated_try"

  df_appointments_view = pd.read_csv(df_appointments_view_path)
  df_appointments_view.drop(columns=["Procedimento","Data"], inplace=True)
  df_appointments_view["Quantidade"] = 1

  # Main served procedeures (3)
  main_served_procedeures = df_appointments_view.loc[df_appointments_view['Mês Atendimento'].isin(Month_list)]
  main_served_procedeures = main_served_procedeures.groupby(["Unidade do agendamento", "Grupo", "Procedimentos Padronizados"]).agg({"Quantidade": "sum"}).reset_index()

  main_served_procedeures = main_served_procedeures.groupby(["Unidade do agendamento"]).head(3)
  main_served_procedeures = main_served_procedeures.sort_values(by=["Unidade do agendamento", "Quantidade"], ascending=[True, False])

  main_served_procedeures

  # time taken from schedule
  time_taken_from_schedule = df_appointments_view.loc[df_appointments_view['Mês Atendimento'].isin(Month_list)]

  # Function to convert "Duração" to seconds
  def convert_to_seconds(duration):
      h, m, s = map(int, duration.split(':'))
      return h * 3600 + m * 60 + s

  #Creating a columns with valus (int) of the minutes taken for each procedure
  time_taken_from_schedule["Duração (s)"] = time_taken_from_schedule["Duração"].apply(convert_to_seconds)
  time_taken_from_schedule["Duração (min)"] = time_taken_from_schedule["Duração (s)"] / 60
  time_taken_from_schedule["Duração (min)"] = time_taken_from_schedule['Duração (min)'].astype(int)

  # Taking off the columns that has the time im str and "procedimento"
  time_taken_from_schedule.drop(columns=["Duração (s)", "Duração"], inplace=True)

  #groupyingby
  time_taken_from_schedule = time_taken_from_schedule.groupby(["Unidade do agendamento","Grupo","Procedimentos Padronizados"]).agg({"Duração (min)": "sum"}).reset_index()
  time_taken_from_schedule


  # direct costs of the period/branch
  direct_costs = df_appointments_view.loc[df_appointments_view['Mês Atendimento'].isin(Month_list)]
  direct_costs = direct_costs.groupby(["Unidade do agendamento","Grupo","Procedimentos Padronizados"]).agg({"Custo Direto": "sum"}).reset_index()
  direct_costs

  #courtesy analysys
  courtesy_analysis = df_appointments_view.loc[df_appointments_view['Mês Atendimento'].isin(Month_list)]
  courtesy_analysis = courtesy_analysis.loc[df_appointments_view['CORTESIA'] == True]

  courtesy_analysis = courtesy_analysis.groupby(["Unidade do agendamento","Grupo","Procedimentos Padronizados"]).agg({"Quantidade": "sum","Custo Direto": "sum"}).reset_index()
  courtesy_analysis = courtesy_analysis.rename(columns={"Quantidade" : "Quantidade (cortesia)", "Custo Direto" : "Custo Direto (corteisa)"})

  #All Indicators - Appointmentes:
  all_indicators_appointments = df_appointments_view.loc[df_appointments_view['Mês Atendimento'].isin(Month_list)]
  all_indicators_appointments = all_indicators_appointments.groupby(["Unidade do agendamento","Grupo","Procedimentos Padronizados"]).agg({"Quantidade": "sum"}).reset_index()

  all_indicators_appointments = all_indicators_appointments.merge(time_taken_from_schedule, on=["Unidade do agendamento","Grupo","Procedimentos Padronizados"], how="left")
  all_indicators_appointments = all_indicators_appointments.merge(direct_costs, on=["Unidade do agendamento","Grupo","Procedimentos Padronizados"], how="left")
  all_indicators_appointments = all_indicators_appointments.merge(courtesy_analysis, on=["Unidade do agendamento","Grupo","Procedimentos Padronizados"], how="left")

  all_indicators_appointments.fillna(0, inplace=True)


  # Saving all DF´s to CSV:
  all_indicators_appointments.to_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/2024/Appointments_View/all_indicators_appointments.csv", index=False)
  main_served_procedeures.to_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/2024/Appointments_View/main_served_procedeures.csv", index=False)
  time_taken_from_schedule.to_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/2024/Appointments_View/time_taken_from_schedule.csv", index=False)
  direct_costs.to_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/2024/Appointments_View/direct_costs.csv", index=False)
  courtesy_analysis.to_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/2024/Appointments_View/courtesy_analysis.csv", index=False)

  return all_indicators_appointments, main_served_procedeures, time_taken_from_schedule, direct_costs, courtesy_analysis
