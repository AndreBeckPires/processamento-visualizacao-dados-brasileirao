import pandas as pd
import numpy as np
from scipy import stats
import csv


def check_outliers_libertadores(dataset):
    liberta = dataset[dataset['Classificacao'] == 'Libertadores']
    z_scores = stats.zscore(liberta['goals_taken'])
    z_limite = 3
    outliers = np.abs(z_scores) > z_limite
    outliers = liberta.iloc[outliers]
    print("Outliers ZSCORE Libertadores:", outliers)

def check_outliers_rebaixamento(dataset):
    rebaixados = dataset[dataset['Classificacao'] == 'Rebaixamento']
    z_scores = stats.zscore(rebaixados['goals'])
    z_limite = 3
    outliers = np.abs(z_scores) > z_limite


    rebaixados_outliers = rebaixados.iloc[outliers]
    print("Outliers ZSCORE Rebaixamentos:", rebaixados_outliers)


def check_outliers_rebaixados_iqr(dataset):
    rebaixados = dataset[dataset['Classificacao'] == 'Rebaixamento']
    q1 = rebaixados['goals'].quantile(0.25)
    q3 = rebaixados['goals'].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    outliers = rebaixados[(rebaixados['goals'] < limite_inferior) | (rebaixados['goals'] > limite_superior)]
    print("Outliers IQR Rebaixamentos:", outliers)


def check_outliers_liberadores_iqr(dataset):
    libertadores = dataset[dataset['Classificacao'] == 'Libertadores'].copy()
    q1 = libertadores['goals_taken'].quantile(0.25)
    q3 = libertadores['goals_taken'].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    outliers = libertadores[(libertadores['goals_taken'] < limite_inferior) | (libertadores['goals_taken'] > limite_superior)]
    print("Outliers IQR Libertadores:", outliers)



def normalizados_rebaixados(dataset):
    rebaixados = dataset[dataset['Classificacao'] == 'Rebaixamento'].copy()
    rebaixados['Gols Marcados Normalizados'] = ((rebaixados['goals'] - rebaixados['goals'].min()) / 
                                                (rebaixados['goals'].max() - rebaixados['goals'].min()))

    rebaixados = rebaixados.sort_values(by='Gols Marcados Normalizados', ascending=True)

    rebaixados.to_csv('csv/normalizados_rebaixados.csv', index=False)

def normalizados_libertadores(dataset):
    libertadores = dataset[dataset['Classificacao'] == 'Libertadores'].copy()
    libertadores['Gols Sofridos Normalizados'] = ((libertadores['goals_taken'] - libertadores['goals_taken'].min()) / 
                                                  (libertadores['goals_taken'].max() - libertadores['goals_taken'].min()))

    libertadores = libertadores.sort_values(by='Gols Sofridos Normalizados', ascending=True)
    libertadores.to_csv('csv/normalizados_liberta.csv', index=False)



