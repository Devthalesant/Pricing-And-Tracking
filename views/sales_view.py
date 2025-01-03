import streamlit as st
import pandas as pd
import os
import random

Month_list = ["Anual","Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
branch_list = ["TODAS","ALPHAVILLE","BELO HORIZONTE","CAMPINAS","COPACABANA","IPIRANGA","ITAIM","JARDINS","LAPA","LONDRINA","MOEMA","MOOCA","OSASCO",
               "RIBEIRÃO PRETO","SANTO AMARO","SANTOS","SOROCABA","SÃO BERNARDO","TATUAPÉ","TIJUCA","TUCURUVI","VILA MASCOTE"]
sales_option = ["Lucro Operacional", "Preço Médio", "Margem de Contribuição","Produtos mais Vendidos", "Quantidade Vendida"]

#Path to the sales indicators CSV file
df_sales_revenue_and_operating_profit_path = "base_de_dados/sales/Sales_View/revenue_and_operating_profit.csv"
df_sales_average_price_path = "base_de_dados/sales/Sales_View/df_average_price.csv"
df_sales_contribution_margin_path = "base_de_dados/sales/Sales_View/df_contribution_margin.csv"
df_sales_main_products_path = "base_de_dados/sales/Sales_View/df_main_products.csv"
df_sales_quantity_sold_path = "base_de_dados/sales/Sales_View/df_quantity_sold.csv"


st.subheader("Visão - Vendas 💎")

sales_option = st.selectbox("O que você quer ver de Vendas?", sales_option)

col_1, col_2 = st.columns(2)

with col_1:
    month_selector = st.multiselect("Escolha o mês", Month_list)
with col_2:
    branch_selector = st.multiselect("Escolha a unidade", branch_list)

if sales_option == "Lucro Operacional":
  df_sales_revenue_and_operating_profit = pd.read_csv(df_sales_revenue_and_operating_profit_path)


  if len(month_selector) == 0 and len(branch_selector) == 0:
    df_sales_revenue_and_operating_profit = df_sales_revenue_and_operating_profit
    st.dataframe(df_sales_revenue_and_operating_profit)

  elif "Anual" in month_selector and "TODAS" in branch_selector:
      st.dataframe(df_sales_revenue_and_operating_profit)

  elif "Anual" in month_selector and "TODAS" not in branch_selector:
      df_sales_revenue_and_operating_profit = df_sales_revenue_and_operating_profit.loc[df_sales_revenue_and_operating_profit['Unidade'].isin(branch_selector)]
      st.dataframe(df_sales_revenue_and_operating_profit)

  elif "Anual" not in month_selector and "TODAS" in branch_selector:
      df_sales_revenue_and_operating_profit = df_sales_revenue_and_operating_profit.loc[df_sales_revenue_and_operating_profit['Mês venda'].isin(month_selector)]
      st.dataframe(df_sales_revenue_and_operating_profit)

  elif "Anual" not in month_selector and "TODAS" not in branch_selector:
      df_sales_revenue_and_operating_profit = df_sales_revenue_and_operating_profit.loc[df_sales_revenue_and_operating_profit['Mês venda'].isin(month_selector) &
                                                                                        df_sales_revenue_and_operating_profit['Unidade'].isin(branch_selector)]
      st.dataframe(df_sales_revenue_and_operating_profit)

elif sales_option == "Preço Médio":
  df_sales_average_price = pd.read_csv(df_sales_average_price_path)

  if len(month_selector) == 0 and len(branch_selector) == 0:
    df_sales_average_price = df_sales_average_price
    st.dataframe(df_sales_average_price)

  elif "Anual" in month_selector and "TODAS" in branch_selector:
      st.dataframe(df_sales_average_price)

  elif "Anual" in month_selector and "TODAS" not in branch_selector:
      df_sales_average_price = df_sales_average_price.loc[df_sales_average_price['Unidade'].isin(branch_selector)]
      st.dataframe(df_sales_average_price)

  elif "Anual" not in month_selector and "TODAS" in branch_selector:
      df_sales_average_price = df_sales_average_price.loc[df_sales_average_price['Mês venda'].isin(month_selector)]
      st.dataframe(df_sales_average_price)

  elif "Anual" not in month_selector and "TODAS" not in branch_selector:
      df_sales_average_price = df_sales_average_price.loc[df_sales_average_price['Mês venda'].isin(month_selector) &
                                                          df_sales_average_price['Unidade'].isin(branch_selector)]
      st.dataframe(df_sales_average_price)

elif sales_option == "Margem de Contribuição":
  df_sales_contribution_margin = pd.read_csv(df_sales_contribution_margin_path)

  if len(month_selector) == 0 and len(branch_selector) == 0:
    df_sales_contribution_margin = df_sales_contribution_margin
    st.dataframe(df_sales_contribution_margin)

  elif "Anual" in month_selector and "TODAS" in branch_selector:
      st.dataframe(df_sales_contribution_margin)

  elif "Anual" in month_selector and "TODAS" not in branch_selector:
      df_sales_contribution_margin = df_sales_contribution_margin.loc[df_sales_contribution_margin['Unidade'].isin(branch_selector)]
      st.dataframe(df_sales_contribution_margin)

  elif "Anual" not in month_selector and "TODAS" in branch_selector:
      df_sales_contribution_margin = df_sales_contribution_margin.loc[df_sales_contribution_margin['Mês venda'].isin(month_selector)]
      st.dataframe(df_sales_contribution_margin)

  elif "Anual" not in month_selector and "TODAS" not in branch_selector:
      df_sales_contribution_margin = df_sales_contribution_margin.loc[df_sales_contribution_margin['Mês venda'].isin(month_selector) &
                                                                      df_sales_contribution_margin['Unidade'].isin(branch_selector)]
      st.dataframe(df_sales_contribution_margin)

elif sales_option == "Produtos mais Vendidos":
  df_sales_main_products = pd.read_csv(df_sales_main_products_path)

  if len(month_selector) == 0 and len(branch_selector) == 0:
    df_sales_main_products = df_sales_main_products
    st.dataframe(df_sales_main_products)

  elif "Anual" in month_selector and "TODAS" in branch_selector:
      st.dataframe(df_sales_main_products)

  elif "Anual" in month_selector and "TODAS" not in branch_selector:
      df_sales_main_products = df_sales_main_products.loc[df_sales_main_products['Unidade'].isin(branch_selector)]
      st.dataframe(df_sales_main_products)

  elif "Anual" not in month_selector and "TODAS" in branch_selector:
      df_sales_main_products = df_sales_main_products.loc[df_sales_main_products['Mês venda'].isin(month_selector)]
      st.dataframe(df_sales_main_products)

  elif "Anual" not in month_selector and "TODAS" not in branch_selector:
      df_sales_main_products = df_sales_main_products.loc[df_sales_main_products['Mês venda'].isin(month_selector) &
                                                          df_sales_main_products['Unidade'].isin(branch_selector)]
      st.dataframe(df_sales_main_products)

elif sales_option == "Quantidade Vendida":
  df_sales_quantity_sold = pd.read_csv(df_sales_quantity_sold_path)

  if len(month_selector) == 0 and len(branch_selector) == 0:
    df_sales_quantity_sold = df_sales_quantity_sold
    st.dataframe(df_sales_quantity_sold)

  elif "Anual" in month_selector and "TODAS" in branch_selector:
      st.dataframe(df_sales_quantity_sold)

  elif "Anual" in month_selector and "TODAS" not in branch_selector:
      df_sales_quantity_sold = df_sales_quantity_sold.loc[df_sales_quantity_sold['Unidade'].isin(branch_selector)]
      st.dataframe(df_sales_quantity_sold)

  elif "Anual" not in month_selector and "TODAS" in branch_selector:
      df_sales_quantity_sold = df_sales_quantity_sold.loc[df_sales_quantity_sold['Mês venda'].isin(month_selector)]
      st.dataframe(df_sales_quantity_sold)

  elif "Anual" not in month_selector and "TODAS" not in branch_selector:
      df_sales_quantity_sold = df_sales_quantity_sold.loc[df_sales_quantity_sold['Mês venda'].isin(month_selector) &
                                                          df_sales_quantity_sold['Unidade'].isin(branch_selector)]
      st.dataframe(df_sales_quantity_sold)

else:
  st.write("Escolha uma opção válida.")
