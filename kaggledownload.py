import kagglehub
import os
import pandas as pd
import matplotlib.pyplot as plt


def download_dataset():
    # Download latest version
    path = kagglehub.dataset_download("regazze/brasileirao-2003-2022")

    print("Path to dataset files:", path)
    print(os.listdir(path))

    excel_file = os.path.join(path, 'brasileirao2.xlsx')
    global df
    df = pd.read_excel(excel_file, engine='openpyxl')

    print(df.head())

def selecionar_atual():
  global formato_atual
  formato_atual = df[df['year'] >= 2006]

def classificar(): 
  print(df.shape)  
  bins = [0,4,6,12,16,20]
  labels = ["Libertadores","Pre-libertadores", "Sul-Americana", "Limbo","Rebaixamento"]
  formato_atual["Classificacao"] = pd.cut(formato_atual['position'], bins=bins, labels=labels, include_lowest=True)

def save_to_csv():
  output_file = "brasileirao_formato_atual_data.csv"
  formato_atual.to_csv(output_file, index=False, encoding='utf-8')
  print(f"Dataset salvo com sucesso em: {output_file}")
  output_file = "dataset_completo.csv"
  df.to_csv(output_file, index=False, encoding='utf-8')
  print(f"Dataset salvo com sucesso em: {output_file}")

def goals_scored_goals_against():
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
  plt.show()

  global sul_americana
  sul_americana = formato_atual[formato_atual['Classificacao'] == 'Sul-Americana']
  grouped_by_year_sula = sul_americana.groupby('year', as_index=True).agg({'goals_scored':'sum',
                                                                     'goals_against':"sum"})
  plt.plot(grouped_by_year_sula.index,grouped_by_year_sula['goals_scored'], marker = 'o')
  plt.plot(grouped_by_year_sula.index,grouped_by_year_sula['goals_against'], marker = 'x')
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos pelos times classificados Sul-Americana")
  plt.show()    

download_dataset()
selecionar_atual()
classificar()
save_to_csv()
#print("First 5 records:", formato_atual.head())
goals_scored_goals_against()