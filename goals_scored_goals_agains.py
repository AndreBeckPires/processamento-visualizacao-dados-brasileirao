import os
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

def goals_scored_goals_against(formato_atual):
  global libertadores
  libertadores = formato_atual[formato_atual['Classificacao'] == 'Libertadores']
  grouped_by_year = libertadores.groupby('year', as_index=True).agg({'goals_scored':'sum',
                                                                     'goals_against':"sum"})


  plt.plot(grouped_by_year.index,grouped_by_year['goals_scored'], marker = 'o', label="Gols Marcados")
  plt.plot(grouped_by_year.index,grouped_by_year['goals_against'], marker = 'x', label="Gols Sofridos")
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos pelos times classificados para Libertadores")
  plt.legend()
  plt.savefig('graficos/classificadosLiberta.png')
  plt.clf() 

  global pre_libertadores
  pre_libertadores = formato_atual[formato_atual['Classificacao'] == 'Pre-libertadores']
  grouped_by_year_pre = pre_libertadores.groupby('year', as_index=True).agg({'goals_scored':'sum',
                                                                     'goals_against':"sum"})
  plt.plot(grouped_by_year_pre.index,grouped_by_year_pre['goals_scored'], marker = 'o', label="Gols Marcados")
  plt.plot(grouped_by_year_pre.index,grouped_by_year_pre['goals_against'], marker = 'x', label="Gols Sofridos")
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos pelos times classificados Pre-Libertadores")
  plt.legend()
  plt.savefig('graficos/classificadosPre.png') 
  plt.clf() 

  global sul_americana
  sul_americana = formato_atual[formato_atual['Classificacao'] == 'Sul-Americana']
  grouped_by_year_sula = sul_americana.groupby('year', as_index=True).agg({'goals_scored':'sum',
                                                                     'goals_against':"sum"})
  plt.plot(grouped_by_year_sula.index,grouped_by_year_sula['goals_scored'], marker = 'o', label="Gols Marcados")
  plt.plot(grouped_by_year_sula.index,grouped_by_year_sula['goals_against'], marker = 'x', label="Gols Sofridos")
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos pelos times classificados Sul-Americana")
  plt.legend()
  plt.savefig('graficos/classificadosSula.png') 
  plt.clf() 

  global rebaixamento
  rebaixamento = formato_atual[formato_atual['Classificacao'] == 'Rebaixamento']
  grouped_by_year_rebaixamento = rebaixamento.groupby('year', as_index=True).agg({'goals_scored':'sum',
                                                                     'goals_against':"sum"})
  plt.plot(grouped_by_year_rebaixamento.index,grouped_by_year_rebaixamento['goals_scored'], marker = 'o', label="Gols Marcados")
  plt.plot(grouped_by_year_rebaixamento.index,grouped_by_year_rebaixamento['goals_against'], marker = 'x', label="Gols Sofridos")
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos pelos times rebaixados")
  plt.legend()
  plt.savefig('graficos/rebaixados.png')  
  plt.clf() 

