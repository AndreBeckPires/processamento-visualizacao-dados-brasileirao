import kaggledownload
import goals_scored_goals_agains
import saldo
import distribuicao

dataset = kaggledownload.download_dataset()
formato_atual = kaggledownload.selecionar_atual(dataset)
formato_atual = kaggledownload.classificar(formato_atual)
kaggledownload.save_to_csv(formato_atual,dataset)
goals_scored_goals_agains.goals_scored_goals_against(formato_atual)
saldo.compare_saldos(formato_atual)
distribuicao.pizza_dist(formato_atual)