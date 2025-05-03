import pandas as pd
import matplotlib.pyplot as plt

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

