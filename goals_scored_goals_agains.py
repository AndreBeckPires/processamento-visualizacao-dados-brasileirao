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
  plt.grid(axis='y', linestyle='--', alpha=0.7)
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
  plt.grid(axis='y', linestyle='--', alpha=0.7)
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
  plt.grid(axis='y', linestyle='--', alpha=0.7)
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
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.savefig('graficos/rebaixados.png')  
  plt.clf() 


  global limbo
  limbo = formato_atual[formato_atual['Classificacao'] == 'Limbo']
  grouped_by_year_limbo = limbo.groupby('year', as_index=True).agg({'goals_scored':'sum',
                                                                     'goals_against':"sum"})
  plt.plot(grouped_by_year_limbo.index,grouped_by_year_limbo['goals_scored'], marker = 'o', label="Gols Marcados")
  plt.plot(grouped_by_year_limbo.index,grouped_by_year_limbo['goals_against'], marker = 'x', label="Gols Sofridos")
  plt.xlabel("Ano")
  plt.ylabel("Gols marcados e sofridos pelos times que não se classificaram para nada")
  plt.legend()
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.savefig('graficos/limbo .png')  
  plt.clf() 

  # gols_marcados = []
  # total_sofridos = []
  # total_gols_libertadores = 0
  # total_gols_pre = 0
  # total_gols_sula = 0
  # total_gols_rebaixamento = 0
  # total_gols_limbo = 0

  # total_gols_sofridos_libertadores = 0
  # total_gols_sofridos_pre = 0
  # total_gols_sofridos_sula = 0
  # total_gols_sofridos_rebaixamento = 0
  # total_gols_sofridos_limbo = 0
 
  # for year in grouped_by_year.index:   
  #   temp = grouped_by_year[grouped_by_year.index == year]
  #   goals = int(temp['goals_scored'].tolist()[0])
  #   goals_sofridos = int(temp['goals_against'].tolist()[0])
  #   total_gols_libertadores += goals
  #   total_gols_sofridos_libertadores += goals_sofridos


  # for year in grouped_by_year_pre.index:   
  #   temp = grouped_by_year_pre[grouped_by_year_pre.index == year]
  #   goals = int(temp['goals_scored'].tolist()[0])
  #   goals_sofridos = int(temp['goals_against'].tolist()[0])
  #   total_gols_pre += goals
  #   total_gols_sofridos_pre += goals_sofridos

  # for year in grouped_by_year_sula.index:   
  #   temp = grouped_by_year_sula[grouped_by_year_sula.index == year]
  #   goals = int(temp['goals_scored'].tolist()[0])
  #   goals_sofridos = int(temp['goals_against'].tolist()[0])
  #   total_gols_sula += goals
  #   total_gols_sofridos_sula += goals_sofridos

  # for year in grouped_by_year_rebaixamento.index:   
  #   temp = grouped_by_year_rebaixamento[grouped_by_year_rebaixamento.index == year]
  #   goals = int(temp['goals_scored'].tolist()[0])
  #   goals_sofridos = int(temp['goals_against'].tolist()[0])
  #   total_gols_rebaixamento += goals
  #   total_gols_sofridos_rebaixamento += goals_sofridos

  
  # for year in grouped_by_year_limbo.index:   
  #   temp = grouped_by_year_limbo[grouped_by_year_limbo.index == year]
  #   goals = int(temp['goals_scored'].tolist()[0])
  #   goals_sofridos = int(temp['goals_against'].tolist()[0])    
  #   total_gols_limbo += goals
  #   total_gols_sofridos_limbo += goals_sofridos

  # classificados = formato_atual[formato_atual['year'] ==  2006]

  # total_classificados_libertadores = classificados[classificados['Classificacao'] == 'Libertadores']
  # total_classificados_libertadores = total_classificados_libertadores['Classificacao'].value_counts()
  # total_classificados_libertadores = total_classificados_libertadores.values




  # total_classificados_pre = classificados[classificados['Classificacao'] == 'Pre-libertadores']
  # total_classificados_pre = total_classificados_pre['Classificacao'].value_counts()
  # total_classificados_pre = total_classificados_pre.values

  # total_classificados_sula = classificados[classificados['Classificacao'] == 'Sul-Americana']
  # total_classificados_sula = total_classificados_sula['Classificacao'].value_counts()
  # total_classificados_sula = total_classificados_sula.values

  # total_rebaixados = classificados[classificados['Classificacao'] == 'Rebaixamento']
  # total_rebaixados = total_rebaixados['Classificacao'].value_counts()
  # total_rebaixados = total_rebaixados.values


  # total_limbo = classificados[classificados['Classificacao'] == 'Limbo']
  # total_limbo = total_limbo['Classificacao'].value_counts()
  # total_limbo = total_limbo.values

  # total_anos = formato_atual['year'].unique()
  # total_anos = total_anos.tolist()

  # media_libertadores = total_gols_libertadores/total_classificados_libertadores[0] 
  # media_libertadores = media_libertadores/len(total_anos)
  # media_pre = total_gols_pre/total_classificados_pre[0]
  # media_pre = media_pre/len(total_anos)
  # media_sula = total_gols_sula/total_classificados_sula[0]
  # media_sula = media_sula/len(total_anos)
  # media_rebaixamento = total_gols_rebaixamento/total_rebaixados[0]
  # media_rebaixamento = media_rebaixamento/len(total_anos)
  # media_limbo = total_gols_limbo/total_limbo[0]
  # media_limbo = media_limbo/len(total_anos)


  # #total_anos = total_anos.value_counts()
  # #media_libertadores = media_libertadores/total_anos




  # media_sofrida_libertadores = total_gols_sofridos_libertadores/total_classificados_libertadores[0]
  # media_sofrida_libertadores = media_sofrida_libertadores/len(total_anos)
  # media_sofrida_pre = total_gols_sofridos_pre/total_classificados_pre[0]
  # media_sofrida_pre = media_sofrida_pre/len(total_anos)
  # media_sofrida_sula = total_gols_sofridos_sula/total_classificados_sula[0]
  # media_sofrida_sula = media_sofrida_sula/len(total_anos)
  # media_sofrida_rebaixaods = total_gols_sofridos_rebaixamento/total_rebaixados[0]
  # media_sofrida_rebaixaods = media_sofrida_rebaixaods/len(total_anos)
  # media_sofrida_limbo = total_gols_sofridos_limbo/total_limbo[0]
  # media_sofrida_limbo = media_sofrida_limbo/len(total_anos)

  # gols_marcados.append(int(media_libertadores))
  # gols_marcados.append(int(media_pre))
  # gols_marcados.append(int(media_sula))
  # gols_marcados.append(int(media_limbo))
  # gols_marcados.append(int(media_rebaixamento))


  # total_sofridos.append(int(media_sofrida_libertadores))
  # total_sofridos.append(int(media_sofrida_pre))
  # total_sofridos.append(int(media_sofrida_sula))
  # total_sofridos.append(int(media_sofrida_limbo))
  # total_sofridos.append(int(media_sofrida_rebaixaods))



  # classificacoes = []
  # for classificacao in classificados['Classificacao'].unique():
  #   classificacoes.append(classificacao)
  
  # plt.bar(classificacoes,gols_marcados)
  # plt.title("Media de gols marcados")
  # plt.grid(axis='y', linestyle='--', alpha=0.7)
  # plt.savefig('graficos/mediagolsmarcados.png')

  # plt.clf()

  # plt.bar(classificacoes,total_sofridos)
  # plt.title("Media de gols sofridos")
  # plt.grid(axis='y', linestyle='--', alpha=0.7)
  # plt.savefig('graficos/mediagolssofridos.png')
  # plt.clf()

  medias = formato_atual.groupby('Classificacao')[['goals_scored','goals_against']].agg('mean')

  plt.figure(figsize=(20, 10))

  plt.bar(medias.index, medias['goals_scored'])
  plt.title("Media de gols marcados")
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.savefig('graficos/mediagolsmarcadosNOVO.png')

  plt.clf()

  plt.bar(medias.index, medias['goals_against'])
  plt.title("Media de gols sofridos")
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.savefig('graficos/mediagolsofridosNOVO.png')

  plt.clf()