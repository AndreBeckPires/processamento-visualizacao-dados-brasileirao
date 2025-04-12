# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import matplotlib.pyplot as plt

# Set the path to the file you'd like to load
file_path = "brasileirao2.xlsx"

def load_data():
# Load the latest version
  global df
  df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "regazze/brasileirao-2003-2022",
    file_path,
    # Provide any additional arguments like 
    # sql_query or pandas_kwargs. See the 
    # documenation for more information:
    # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
  )


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
  




load_data()
selecionar_atual()
classificar()
save_to_csv()
#print("First 5 records:", formato_atual.head())
goals_scored_goals_against()