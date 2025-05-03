import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder

def grafico_linha(titulo, label_x, label_y, dataset1, label1, cor1, nome, dataset2 = None, label2 = None, cor2 = None):
    plt.figure(figsize=(10, 5))
    plt.plot(dataset1.index, dataset1.values, marker='o', label=label1,  linestyle='-', color=cor1)
    if dataset2  is not None:
        plt.plot(dataset2.index, dataset2.values, marker='s', label=label2, color=cor2, linestyle='--')
    plt.xticks(ticks=dataset1.index.astype(int))
    plt.title(titulo)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.grid(True)
    plt.savefig(f'graficos/{nome}')

def set_regioes(atual, path):
    times = pd.read_csv(path)
    atributos_times = times[['team', 'full_name', 'city', 'state', 'region']]
    atual = pd.merge(atual, atributos_times, on='team', how='left')

    output_file = "csv/brasileirao_formato_atual_data_com_regioes.csv"
    atual.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Dataset salvo com sucesso em: {output_file}")
    return atual


def grafico_barras_horizontal(dataset, titulo, cor, label_x, label_y, nome):
    plt.figure(figsize=(15, 6))
    plt.tight_layout()
  
    dataset.sort_values().plot(kind='barh', color=cor)
    plt.title(titulo, fontsize = 16)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.savefig(f'graficos/{nome}')

def grafico_pizza(dataset, titulo,nome):
    plt.figure(figsize=(8, 8))
    plt.pie(
        dataset,
        labels=dataset.index,
        autopct='%1.1f%%',
        startangle=140
    )
    plt.title(titulo)
    plt.axis('equal')  # Deixa o gráfico circular

    plt.savefig(f'graficos/{nome}')


def maiores_vencedores(atual):
    campeoes = atual[atual['place'] == 1]
    vencedores = campeoes['team'].value_counts()

    grafico_barras_horizontal(vencedores, 'Maiores Vencedores (Número de Títulos)', 'skyblue', 'Títulos', 'Time','maioresvencedores.png')


def mais_pontos(atual):
    pontosTotais = atual.groupby('team')['points'].sum().sort_values()
    corte = pontosTotais.quantile(0.30)
    pontuadores_top70 = pontosTotais[pontosTotais > corte].sort_values()

    grafico_barras_horizontal(pontuadores_top70, 'Maiores Pontuadores - Top 70%', 'skyblue', 'Pontos', 'Time', 'maiorespontuadores.png' )

def mais_gols_feitos(atual):
    golsTotais = atual.groupby('team')['goals'].sum().sort_values(ascending=False).head(20)

    grafico_barras_horizontal(golsTotais, 'Maiores Goleadores - Top 20', 'green', 'Gols', 'Time','maisgols.png')

def mais_gols_sofridos(atual):
    golsContra = atual.groupby('team')['goals_taken'].sum().sort_values(ascending=False).head(20)

    grafico_barras_horizontal(golsContra, 'Gols Sofridos - Top 20','red','Gols', 'Time','mais_gols_sofridos.png')    

def mais_derrotas(atual):
    derrotas = atual.groupby('team')['loss'].sum().sort_values(ascending=False).head(20)

    grafico_barras_horizontal(derrotas, 'Derrotas - Top 20', 'red', 'Derrotas', 'Time', 'mais_derrotas.png')

def mais_rebaixados(atual):
    rebaixados = atual[atual['place'] > 16]
    rebaixados = rebaixados['team'].value_counts()

    grafico_barras_horizontal(rebaixados, 'Maiores Rebaixados' ,'orange', 'Rebaixamentos', 'Time', 'mais_rebaixados.png')

def mais_participacoes(atual):
    participacoes = atual.groupby('team')['season'].nunique().sort_values(ascending=False)

    grafico_barras_horizontal(participacoes, 'Participações', 'yellow', 'Participações','Time','mais_participacoes.png')

def camp_por_regiao(atual):
    campeoes = atual[atual['place'] == 1]
    campeoes_por_regiao = campeoes['region'].value_counts()

    grafico_pizza(campeoes_por_regiao, 'Campeões por Região','campeoes_por_regiao.png')

def camp_por_estado(atual):
    campeoes = atual[atual['place'] == 1]
    campeoes_por_estado = campeoes['state'].value_counts()

    grafico_pizza(campeoes_por_estado, 'Campeões por Estado', 'campeos_por_estado.png')

def gols_por_regiao(atual):
    gols_por_regiao = atual.groupby('region')['goals'].sum().sort_values(ascending=False)

    # Remove regiões com valor NaN (caso existam)
    gols_por_regiao = gols_por_regiao.dropna()

    grafico_pizza(gols_por_regiao, 'Gols por Região','gols_por_regiao.png')

def total_gols(atual):
    gols_por_temporada = atual.groupby('season')['goals'].sum().sort_index()

    grafico_linha('Total de gols por temporada', 'Temporada', 'Total de Gols', gols_por_temporada, 'Total de gols por temporada', 'blue','total_gols_temporada.png')
    media_gols_por_temporada = atual.groupby('season')['goals'].mean().sort_index()

    grafico_linha('Média de gols por temporada', 'Temporada', 'Média de Gols', media_gols_por_temporada, 'Média', 'green','media_gols_temporada.png')

def gols_campeao_rebaixado(atual):
    campeoes = atual[atual['place'] == 1]
    pontos_campeao = campeoes.groupby('season')['points'].first().sort_index()
    pontos_salvacao = atual[atual['place'] == 16].groupby('season')['points'].first().sort_index()

    grafico_linha('Necessidade de Pontos', 'Temporada', 'Pontos', pontos_campeao, 'Campeão', 'green','gols_campeao_rebaixado.png', pontos_salvacao , 'Salvo', 'orange')

def analise_qualidade(atual):
    print("Soma de valores vazios: ")
    print(atual.isna().sum())
    linhas_com_nan = atual[atual.isna().any(axis=1)]
    print("Linhas com NaN: ")
    print(linhas_com_nan)
    duplicated = atual.duplicated()
    print("Duplicados: ")
    print(duplicated.sum())

def print_solucao_drop_na(atual):
    atual = atual.dropna()
    print("########")
    print("Solução drop NA: ")
    print("Soma de valores vazios: ")
    print(atual.isna().sum())
    linhas_com_nan = atual[atual.isna().any(axis=1)]
    print("Linhas com NaN: ")
    print(linhas_com_nan)
    duplicated = atual.duplicated()
    print("Duplicados: ")
    print(duplicated.sum())

def print_solucao_complete(atual):
    atual['team'] = atual['team'].fillna('Gremio Barueri')
    atual['full_name'] = atual['full_name'].fillna('Gremio Barueri Futebol Ltda')
    atual['city'] = atual['city'].fillna('Barueri')
    atual['state'] = atual['state'].fillna('Sao Paulo')
    atual['region'] = atual['region'].fillna('EixoRJ-SP')
    print("########")
    print("Solução 'COMPLETE': ")
    print("Soma de valores vazios: ")
    print(atual.isna().sum())
    linhas_com_nan = atual[atual.isna().any(axis=1)]
    print("Linhas com NaN: ")
    print(linhas_com_nan)
    duplicated = atual.duplicated()
    print("Duplicados: ")
    print(duplicated.sum())
    
def gols_sofridos_do_segundo_colocado_por_temporada(atual):
    vices = atual[atual['place'] == 2]
    gols_sofridos_por_temporada = vices.groupby('season')['goals_taken'].first().sort_index()

    grafico_linha('Gols sofridos pelo Vice', 'Temporada', 'Nro Gols Sofridos', gols_sofridos_por_temporada, 'Gols', 'red','sofridos_segundo_lugar.png') 
    return vices

def vices_grafico_dispersao(vices):

    plt.figure(figsize=(10, 10))

    plt.scatter(vices["goals_taken"], vices["season"], color="skyblue", alpha=0.7, edgecolor="black")
    plt.scatter(vices["goals_diff"], vices["season"], color="orange", alpha=0.7, edgecolor="black")

    plt.title("Gols sofridos pelo Vice e Saldo", fontsize=16)
    plt.xlabel("Qtd Gols", fontsize=12)
    plt.ylabel("Ano", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(fontsize=10)
    plt.yticks(ticks=vices.season.astype(int))
    plt.yticks(fontsize=10)
    plt.savefig('graficos/grafico_dispersao.png') 


def oneHot_enconding(atual):
    categorias = atual[['region']]

    encoder = OneHotEncoder(sparse_output=False)
    categorias_encoded = encoder.fit_transform(categorias)

    feature_names = encoder.get_feature_names_out(categorias.columns)
    categorias_encoded_df = pd.DataFrame(categorias_encoded, columns=feature_names)

    categorias_encoded_df.index = atual.index
    atual = atual.drop(columns=categorias.columns)
    atual = pd.concat([atual, categorias_encoded_df], axis=1)

    output_file = "csv/oneHOT.csv"
    atual.to_csv(output_file, index=False, encoding='utf-8')
