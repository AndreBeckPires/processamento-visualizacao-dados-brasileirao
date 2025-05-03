import os
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

def goals_scored_goals_taken(formato_atual):
  formato_atual['season'] = formato_atual['season'].astype(int)
  global libertadores
  libertadores = formato_atual[formato_atual['Classificacao'] == 'Libertadores']
  grouped_by_year = libertadores.groupby('season', as_index=True).agg({'goals':'sum',
                                                                     'goals_taken':"sum"})


  plt.plot(grouped_by_year.index,grouped_by_year['goals'], marker = 'o', label="Gols Marcados")
  plt.plot(grouped_by_year.index,grouped_by_year['goals_taken'], marker = 'x', label="Gols Sofridos")
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos - classificados para Libertadores")
  plt.xticks(grouped_by_year.index)
  plt.xticks(rotation=45)

  plt.tight_layout()
  
  plt.legend()
  plt.grid(axis='y', linestyle='--', alpha=0.7)


  plt.savefig('graficos/classificadosLiberta.png')
  plt.clf() 

  global pre_libertadores
  pre_libertadores = formato_atual[formato_atual['Classificacao'] == 'Pre-libertadores']
  grouped_by_year_pre = pre_libertadores.groupby('season', as_index=True).agg({'goals':'sum',
                                                                     'goals_taken':"sum"})
  plt.plot(grouped_by_year_pre.index,grouped_by_year_pre['goals'], marker = 'o', label="Gols Marcados")
  plt.plot(grouped_by_year_pre.index,grouped_by_year_pre['goals_taken'], marker = 'x', label="Gols Sofridos")
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos - classificados Pre-Libertadores")
  plt.xticks(grouped_by_year_pre.index)
  plt.legend()
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.xticks(rotation=45)

  plt.savefig('graficos/classificadosPre.png') 
  plt.clf() 

  global sul_americana
  sul_americana = formato_atual[formato_atual['Classificacao'] == 'Sul-Americana']
  grouped_by_year_sula = sul_americana.groupby('season', as_index=True).agg({'goals':'sum',
                                                                     'goals_taken':"sum"})
  plt.plot(grouped_by_year_sula.index,grouped_by_year_sula['goals'], marker = 'o', label="Gols Marcados")
  plt.plot(grouped_by_year_sula.index,grouped_by_year_sula['goals_taken'], marker = 'x', label="Gols Sofridos")
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos - classificados Sul-Americana")
  plt.xticks(grouped_by_year_sula.index)
  plt.legend()
  plt.xticks(rotation=45)

  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.savefig('graficos/classificadosSula.png')
  plt.clf() 

  global rebaixamento
  rebaixamento = formato_atual[formato_atual['Classificacao'] == 'Rebaixamento']
  grouped_by_year_rebaixamento = rebaixamento.groupby('season', as_index=True).agg({'goals':'sum',
                                                                     'goals_taken':"sum"})
  plt.plot(grouped_by_year_rebaixamento.index,grouped_by_year_rebaixamento['goals'], marker = 'o', label="Gols Marcados")
  plt.plot(grouped_by_year_rebaixamento.index,grouped_by_year_rebaixamento['goals_taken'], marker = 'x', label="Gols Sofridos")
  plt.xticks(grouped_by_year_rebaixamento.index)
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofrido - times rebaixados")
  plt.xticks(rotation=45)

  plt.legend()
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.savefig('graficos/rebaixados.png')  
  plt.clf() 


  global limbo
  limbo = formato_atual[formato_atual['Classificacao'] == 'Limbo']
  grouped_by_year_limbo = limbo.groupby('season', as_index=True).agg({'goals':'sum',
                                                                     'goals_taken':"sum"})
  plt.plot(grouped_by_year_limbo.index,grouped_by_year_limbo['goals'], marker = 'o', label="Gols Marcados")
  plt.plot(grouped_by_year_limbo.index,grouped_by_year_limbo['goals_taken'], marker = 'x', label="Gols Sofridos")
  plt.xticks(grouped_by_year_limbo.index)
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos - não se classificaram para nada")
  plt.legend()
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.xticks(rotation=45)

  plt.savefig('graficos/limbo .png')  
  plt.clf() 

 
  medias = formato_atual.groupby('Classificacao')[['goals','goals_taken']].agg('mean')

  plt.figure(figsize=(20, 10))

  plt.bar(medias.index, medias['goals'])
  plt.title("Media de gols marcados")
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.savefig('graficos/mediagolsmarcadosNOVO.png')

  plt.clf()

  plt.bar(medias.index, medias['goals_taken'])
  plt.title("Media de gols sofridos")
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.savefig('graficos/mediagolsofridosNOVO.png')

  plt.clf()