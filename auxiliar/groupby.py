from pymongo import MongoClient, UpdateOne
import pandas as pd
import re


def grafico_barras_vendas(new_df): 
  new_df['DATA'] = pd.to_datetime(new_df['DATA'])
  new_df['PERIODO'] = new_df['DATA'].dt.to_period('M')

  barras_df = new_df.groupby(['PERIODO']).agg({'TOTAL LÍQUIDO ITEM': 'sum'})

  return barras_df
