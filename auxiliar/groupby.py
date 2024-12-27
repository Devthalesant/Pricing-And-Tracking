from pymongo import MongoClient, UpdateOne
import pandas as pd
import re
import plotly.express as px


def grafico_barras_vendas(new_df): 
  new_df['DATA'] = pd.to_datetime(new_df['DATA'])
  #tirar hora depois
  new_df['PERIODO'] = new_df['DATA'].dt.to_period('M')

  barras_df = new_df.groupby(['PERIODO']).agg({'TOTAL LÍQUIDO ITEM': 'sum'})

  fig = px.bar(
            new_df,
            x='PERIODO',
            y='TOTAL LÍQUIDO ITEM',
            title='GRÁFICO VENDAS GERAL'
        )

  return fig
