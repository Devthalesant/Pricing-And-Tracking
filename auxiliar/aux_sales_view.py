
import streamlit as st
import pandas as pd
import os

def sales_view():

  Month_list = ["janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro"]
  branches_list = ['ALPHAVILLE','BELO HORIZONTE','CAMPINAS','COPACABANA','IPIRANGA','ITAIM','JARDINS','LAPA','LONDRINA','MOEMA','MOOCA','OSASCO','RIBEIRÃO PRETO','SANTO AMARO','SANTOS','SOROCABA','SÃO BERNARDO','TATUAPÉ','TIJUCA','TUCURUVI','VILA MASCOTE']


  # DF Sales Concatenated Paths
  df_sales_view_path = "/content/drive/MyDrive/python - Thales/P&T/Bases CSV/ALL/data_sales_2024_updated_try.csv"

  # DF Sales
  df_sales_view = pd.read_csv(df_sales_view_path)

  # Average price charged
  df_average_price = df_sales_view.loc[df_sales_view['Mês venda'].isin(Month_list)]
  df_average_price = df_average_price.loc[df_sales_view['CORTESIA'] != True]
  df_average_price = df_average_price.groupby(["Unidade", "Grupo", "Procedimentos Padronizados"]).agg({"Valor liquido": "mean"}).reset_index()
  df_average_price.rename(columns={"Valor liquido": "Preço médio"}, inplace=True)
  df_average_price['Preço médio'] = df_average_price['Preço médio'].round(2)

  # Quantity sold
  #converting the columns Quantidade to Int
  df_quantity_sold = df_sales_view.loc[df_sales_view['Mês venda'].isin(Month_list)]
  df_quantity_sold = df_quantity_sold.loc[df_sales_view['CORTESIA'] != True]
  df_quantity_sold = df_quantity_sold.groupby(["Unidade", "Grupo", "Procedimentos Padronizados"]).agg({"Quantidade": "sum"}).reset_index()
  df_quantity_sold

  #Contribution margin
  df_contribution_margin = df_sales_view.loc[df_sales_view['Mês venda'].isin(Month_list)]
  df_contribution_margin = df_contribution_margin.loc[df_sales_view['CORTESIA'] != True]
  taxa_cartão  = 0.1121
  taxa_comissao = 0.04
  taxa_imposto = 0.1425
  taxa_total = taxa_cartão + taxa_comissao + taxa_imposto
  df_contribution_margin["Margem de Contribuição (R$)"] = df_contribution_margin["Valor liquido item"] - df_contribution_margin["Custo Direto"] - (df_contribution_margin["Valor liquido item"] * taxa_total)
  df_contribution_margin = df_contribution_margin.groupby(["Unidade", "Grupo", "Procedimentos Padronizados"]).agg({"Valor liquido item" : "sum" ,"Margem de Contribuição (R$)": "sum"}).reset_index()

  df_contribution_margin["Margem de Contribuição (%)"] = df_contribution_margin["Margem de Contribuição (R$)"] / df_contribution_margin["Valor liquido item"] * 100

  df_contribution_margin['Margem de Contribuição (R$)'] = df_contribution_margin['Margem de Contribuição (R$)'].round(2)
  df_contribution_margin['Valor liquido item'] = df_contribution_margin['Valor liquido item'].round(2)

  df_contribution_margin.style.format({"Margem de Contribuição (%)": "{:.2f}%"})

  # Main products sold in each branch and the indicators above
  df_main_products = df_sales_view.loc[df_sales_view['Mês venda'].isin(Month_list)]
  df_main_products = df_main_products.loc[df_sales_view['CORTESIA'] != True]
  df_main_products = df_main_products.groupby(["Unidade", "Grupo", "Procedimentos Padronizados"]).agg({"Quantidade": "sum"}).reset_index()
  df_main_products = df_main_products.sort_values(by="Quantidade", ascending=False)

  df_main_products = df_main_products.groupby(["Unidade"]).head(3)
  df_main_products = df_main_products.sort_values(by=["Unidade", "Quantidade"], ascending=[True, False])

  df_main_products_test = pd.merge(df_main_products, df_contribution_margin[['Unidade', 'Grupo', 'Procedimentos Padronizados', 'Valor liquido item', 'Margem de Contribuição (R$)', 'Margem de Contribuição (%)']],
                      on=['Unidade', 'Grupo', 'Procedimentos Padronizados'],
                      how='left')

  df_main_products_test

  # All indicator Sales
  all_indicators_sales = df_sales_view.loc[df_sales_view['Mês venda'].isin(Month_list)]
  all_indicators_sales = all_indicators_sales.loc[df_sales_view['CORTESIA'] != True]
  all_indicators_sales = all_indicators_sales.groupby(["Unidade", "Grupo", "Procedimentos Padronizados"]).agg({"Quantidade": "sum"}).reset_index()

  all_indicators_sales = pd.merge(all_indicators_sales, df_contribution_margin[['Unidade', 'Grupo', 'Procedimentos Padronizados', 'Valor liquido item', 'Margem de Contribuição (R$)', 'Margem de Contribuição (%)']],
                      on=['Unidade', 'Grupo', 'Procedimentos Padronizados'],
                      how='left')

  all_indicators_sales = pd.merge(all_indicators_sales,
                      df_average_price[['Unidade', 'Grupo', 'Procedimentos Padronizados', 'Preço médio']],
                      on=['Unidade', 'Grupo', 'Procedimentos Padronizados'],
                      how='left')

  # Sorting values by Branch and sold Quantity
  all_indicators_sales = all_indicators_sales.sort_values(by=["Unidade", "Quantidade"], ascending=[True, False])

  # Saving all DF´s to CSV:
  all_indicators_sales.to_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/2024/Sales_View/all_indicators_sales.csv", index=False)
  df_average_price.to_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/2024/Sales_View/df_average_price.csv", index=False)
  df_quantity_sold.to_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/2024/Sales_View/df_quantity_sold.csv", index=False)
  df_contribution_margin.to_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/2024/Sales_View/df_contribution_margin.csv", index=False)
  df_main_products.to_csv("/content/drive/MyDrive/python - Thales/P&T/Bases CSV/2024/Sales_View/df_main_products.csv", index=False)

  return all_indicators_sales, df_average_price, df_quantity_sold, df_contribution_margin, df_main_products
