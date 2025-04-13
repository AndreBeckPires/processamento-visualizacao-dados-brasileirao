import kagglehub
import os
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import shutil

def download_dataset():
    # Download latest version
    path = kagglehub.dataset_download("regazze/brasileirao-2003-2022")

    print("Path to dataset files:", path)
    print(os.listdir(path))

    for file in os.listdir(path):
      original = os.path.join(path, file)
      destiny = os.path.join('csv', file)
      shutil.copy2(original, destiny)
      
    excel_file = os.path.join(destiny)
    global df
    df = pd.read_excel(excel_file, engine='openpyxl')

    print(df.head())
    return df

def selecionar_atual(df):
  global formato_atual
  formato_atual = df[df['year'] >= 2006]
  return formato_atual

def classificar(formato_atual): 
  print(df.shape)  
  bins = [0,4,6,12,16,20]
  labels = ["Libertadores","Pre-libertadores", "Sul-Americana", "Limbo","Rebaixamento"]
  formato_atual["Classificacao"] = pd.cut(formato_atual['position'], bins=bins, labels=labels, include_lowest=True)
  return formato_atual

def save_to_csv(formato_atual, df):
  output_file = "csv/brasileirao_formato_atual_data.csv"
  formato_atual.to_csv(output_file, index=False, encoding='utf-8')
  print(f"Dataset salvo com sucesso em: {output_file}")
  output_file = "csv/dataset_completo.csv"
  df.to_csv(output_file, index=False, encoding='utf-8')
  print(f"Dataset salvo com sucesso em: {output_file}")

def goals_scored_goals_against(formato_atual):
  global libertadores
  libertadores = formato_atual[formato_atual['Classificacao'] == 'Libertadores']
  grouped_by_year = libertadores.groupby('year', as_index=True).agg({'goals_scored':'sum',
                                                                     'goals_against':"sum"})
  print(grouped_by_year.head())
  #scored_goals = libertadores['goals_scored'].tolist()
  #print(scored_goals)
   

  plt.plot(grouped_by_year.index,grouped_by_year['goals_scored'], marker = 'o')
  plt.plot(grouped_by_year.index,grouped_by_year['goals_against'], marker = 'x')
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos pelos times classificados para Libertadores")
  plt.savefig('classificadosLiberta.png')
  plt.clf() 

  global pre_libertadores
  pre_libertadores = formato_atual[formato_atual['Classificacao'] == 'Pre-libertadores']
  grouped_by_year_pre = pre_libertadores.groupby('year', as_index=True).agg({'goals_scored':'sum',
                                                                     'goals_against':"sum"})
  plt.plot(grouped_by_year_pre.index,grouped_by_year_pre['goals_scored'], marker = 'o')
  plt.plot(grouped_by_year_pre.index,grouped_by_year_pre['goals_against'], marker = 'x')
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos pelos times classificados Pre-Libertadores")
  plt.savefig('classificadosPre.png') 
  plt.clf() 

  global sul_americana
  sul_americana = formato_atual[formato_atual['Classificacao'] == 'Sul-Americana']
  grouped_by_year_sula = sul_americana.groupby('year', as_index=True).agg({'goals_scored':'sum',
                                                                     'goals_against':"sum"})
  plt.plot(grouped_by_year_sula.index,grouped_by_year_sula['goals_scored'], marker = 'o')
  plt.plot(grouped_by_year_sula.index,grouped_by_year_sula['goals_against'], marker = 'x')
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos pelos times classificados Sul-Americana")
  plt.savefig('classificadosSula.png') 
  plt.clf() 

  global rebaixamento
  rebaixamento = formato_atual[formato_atual['Classificacao'] == 'Rebaixamento']
  grouped_by_year_rebaixamento = rebaixamento.groupby('year', as_index=True).agg({'goals_scored':'sum',
                                                                     'goals_against':"sum"})
  plt.plot(grouped_by_year_rebaixamento.index,grouped_by_year_rebaixamento['goals_scored'], marker = 'o')
  plt.plot(grouped_by_year_rebaixamento.index,grouped_by_year_rebaixamento['goals_against'], marker = 'x')
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos pelos times rebaixados")
  plt.savefig('rebaixados.png')  
  plt.clf() 

