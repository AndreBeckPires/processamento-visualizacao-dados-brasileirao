import pandas as pd
import numpy as np
from scipy.stats import zscore

# puxa o dataset do keaggle 
url = 'https://raw.githubusercontent.com/regazze/brasileirao-2003-2022/main/brasileirao-2003-2022.csv'
df = pd.read_csv(url)

# Converter datas
df['data'] = pd.to_datetime(df['data'])
df['ano'] = df['data'].dt.year
df['mandante_gols'] = df['mandante placar']
df['visitante_gols'] = df['visitante placar']

# Gols por time dentro de casa
gols_mandante = df.groupby(['ano', 'mandante'])['mandante_gols'].sum().reset_index()
gols_mandante.columns = ['ano', 'time', 'gols']

# Gols por time fora de casa
gols_visitante = df.groupby(['ano', 'visitante'])['visitante_gols'].sum().reset_index()
gols_visitante.columns = ['ano', 'time', 'gols']

# Total de gols da equipe
gols_total = pd.concat([gols_mandante, gols_visitante])
gols_total = gols_total.groupby(['ano', 'time'])['gols'].sum().reset_index()

# ultimo jogo para definir a posição
df['rodada'] = pd.to_numeric(df['rodada'], errors='coerce')
ultimas_rodadas = df.groupby('ano')['rodada'].transform('max')
tabela_final = df[df['rodada'] == ultimas_rodadas]
posicoes_finais = tabela_final[['ano', 'mandante', 'colocacao']].drop_duplicates()
posicoes_finais.columns = ['ano', 'time', 'colocacao']

# Juntar com os dados de gols
dados = pd.merge(gols_total, posicoes_finais, on=['ano', 'time'], how='inner')

# Separar campeões e rebaixados
campeoes = dados[dados['colocacao'] == 1].copy()
rebaixados = dados[dados['colocacao'] >= 17].copy()  # Rebaixados podem ser de 17º a 20º

# Juntar em um único dataframe
todos = pd.concat([campeoes.assign(tipo='campeao'), rebaixados.assign(tipo='rebaixado')])

# Calcular Z-score por ano
todos['zscore_gols'] = todos.groupby('ano')['gols'].transform(lambda x: zscore(x, nan_policy='omit'))

# Detectar outliers
outliers = todos[np.abs(todos['zscore_gols']) > 2]

# Exibir os outliers
print("Outliers entre campeões e rebaixados com base nos gols:")
print(outliers[['ano', 'time', 'tipo', 'gols', 'zscore_gols']])

