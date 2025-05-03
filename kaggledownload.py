import kagglehub
import os
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import shutil

def download_dataset():
    # Download latest version
    path = kagglehub.dataset_download("lucasyukioimafuko/brasileirao-serie-a-2006-2022")

    print("Path to dataset files:", path)
    print(os.listdir(path))

    for file in os.listdir(path):
      original = os.path.join(path, file)
      destiny = os.path.join('csv', file)
      shutil.copy2(original, destiny)
      

    global df
    df = pd.read_csv('csv/brasileirao.csv') 


    print(df.head())
    return df

def selecionar_atual(df):
  global formato_atual
  formato_atual = df[df['season'] >= 2006]
  return formato_atual

def classificar(formato_atual): 
  #print(df.shape)  
  bins = [0,4,6,12,16,20]
  labels = ["Libertadores","Pre-libertadores", "Sul-Americana", "Limbo","Rebaixamento"]
  formato_atual["Classificacao"] = pd.cut(formato_atual['place'], bins=bins, labels=labels, include_lowest=True)
  return formato_atual

def save_to_csv(formato_atual, df):
  output_file = "csv/brasileirao_formato_atual_data.csv"
  formato_atual.to_csv(output_file, index=False, encoding='utf-8')
  print(f"Dataset salvo com sucesso em: {output_file}")
  output_file = "csv/dataset_completo.csv"
  df.to_csv(output_file, index=False, encoding='utf-8')
  print(f"Dataset salvo com sucesso em: {output_file}")

