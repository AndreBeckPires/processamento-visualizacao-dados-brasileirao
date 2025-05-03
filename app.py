import kaggledownload
import goals_scored_goals_agains
import saldo
import distribuicao
import outliers
import times

dataset = kaggledownload.download_dataset()
formato_atual = kaggledownload.selecionar_atual(dataset)
formato_atual = kaggledownload.classificar(formato_atual)
kaggledownload.save_to_csv(formato_atual,dataset)
goals_scored_goals_agains.goals_scored_goals_taken(formato_atual)
saldo.compare_saldos(formato_atual)
distribuicao.pizza_dist(formato_atual)
outliers.check_outliers_libertadores(formato_atual)
outliers.check_outliers_rebaixamento(formato_atual)
outliers.check_outliers_rebaixados_iqr(formato_atual)
outliers.check_outliers_liberadores_iqr(formato_atual)
outliers.normalizados_rebaixados(formato_atual)
outliers.normalizados_libertadores(formato_atual)
com_regioes = times.set_regioes(formato_atual,'/Users/beckreichert/Documents/Codigos/processamento e visualizaçao de dados/csv/teams.csv')
times.maiores_vencedores(com_regioes)
times.mais_pontos(com_regioes)
times.mais_gols_feitos(com_regioes)
times.mais_gols_sofridos(com_regioes)
times.mais_derrotas(com_regioes)