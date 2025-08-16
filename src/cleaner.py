import pandas as pd

def clean_data(df):
  df = df.drop_duplicates()
  df = df.dropna(thresh=int(0.05 * len(df.columns)))
  df.columns = [col.strip().lower.replace(" ", "_') for col in df.columns]
  return df
