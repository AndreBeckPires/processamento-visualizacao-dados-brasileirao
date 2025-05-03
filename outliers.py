import pandas as pd
import numpy as np
from scipy import stats
import csv

# puxa o dataset do keaggle 
# url = 'https://raw.githubusercontent.com/regazze/brasileirao-2003-2022/main/brasileirao-2003-2022.csv'
# df = pd.read_csv(url)
def check_outliers_libertadores(dataset):
    liberta = dataset[dataset['Classificacao'] == 'Libertadores']
    z_scores = stats.zscore(liberta['goals_against'])
    z_limite = 3
    outliers = np.abs(z_scores) > z_limite
    outliers = liberta.iloc[outliers]
    print("Outliers ZSCORE Libertadores:", outliers)

def check_outliers_rebaixamento(dataset):
    rebaixados = dataset[dataset['Classificacao'] == 'Rebaixamento']
    z_scores = stats.zscore(rebaixados['goals_scored'])
    z_limite = 3
    outliers = np.abs(z_scores) > z_limite


    rebaixados_outliers = rebaixados.iloc[outliers]
    print("Outliers ZSCORE Rebaixamentos:", rebaixados_outliers)


def check_outliers_rebaixados_iqr(dataset):
    rebaixados = dataset[dataset['Classificacao'] == 'Rebaixamento']
    q1 = rebaixados['goals_scored'].quantile(0.25)
    q3 = rebaixados['goals_scored'].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    outliers = rebaixados[(rebaixados['goals_scored'] < limite_inferior) | (rebaixados['goals_scored'] > limite_superior)]
    print("Outliers IQR Rebaixamentos:", outliers)


def check_outliers_liberadores_iqr(dataset):
    libertadores = dataset[dataset['Classificacao'] == 'Libertadores'].copy()
    q1 = libertadores['goals_against'].quantile(0.25)
    q3 = libertadores['goals_against'].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    outliers = libertadores[(libertadores['goals_against'] < limite_inferior) | (libertadores['goals_against'] > limite_superior)]
    print("Outliers IQR Libertadores:", outliers)



def normalizados_rebaixados(dataset):
    rebaixados = dataset[dataset['Classificacao'] == 'Rebaixamento'].copy()
    rebaixados['Gols Marcados Normalizados'] = (rebaixados['goals_scored'] - rebaixados['goals_scored'].min()) / (rebaixados['goals_scored'].max() - rebaixados['goals_scored'].min())
   # print("Top 5 normalizados 'Rebaixados' mais altos:")
   #print(rebaixados.nlargest(5, 'Gols Marcados Normalizados'))

   # print("\nTop 5 normalizados 'Rebaixados' mais baixos:")
   # print(rebaixados.nsmallest(5, 'Gols Marcados Normalizados'))
    rebaixados = rebaixados.sort_values(by='Gols Marcados Normalizados', ascending=True)

    rebaixados.to_csv('csv/normalizados_rebaixados.csv', index=False)

def normalizados_libertadores(dataset):
    libertadores = dataset[dataset['Classificacao'] == 'Libertadores'].copy()
    libertadores['Gols Sofridos Normalizados'] = (libertadores['goals_against'] - libertadores['goals_against'].min()) / (libertadores['goals_against'].max() - libertadores['goals_against'].min())
    #print("Top 5 normalizados 'Libertadores' mais altos:")
   # print(libertadores.nlargest(5, 'Gols Sofridos Normalizados'))

   # print("\nTop 5 normalizados 'Libertadores' mais baixos:")
   # print(libertadores.nsmallest(5, 'Gols Sofridos Normalizados'))
    libertadores = libertadores.sort_values(by='Gols Sofridos Normalizados', ascending=True)
    libertadores.to_csv('csv/normalizados_liberta.csv', index=False)



