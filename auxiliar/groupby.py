from pymongo import MongoClient, UpdateOne
import pandas as pd
import re
import plotly.express as px


def grafico_barras_vendas(new_df): 
  new_df['DATA'] = pd.to_datetime(new_df['DATA'])
  #tirar hora depois
  new_df['MES/ANO'] = new_df['DATA'].dt.to_period('M')

  barras_df = new_df.groupby(['MES/ANO']).agg({'TOTAL LÍQUIDO ITEM': 'sum'})
  barras_df['MES/ANO'] = barras_df['MES/ANO'].astype(str)

  fig = px.bar(
            new_df,
            x='MES/ANO',
            y='TOTAL LÍQUIDO ITEM',
            title='GRÁFICO VENDAS GERAL'
        )

  return fig
