import matplotlib.pyplot as plt

def compare_saldos(formato_atual):
    grouped_by_year = formato_atual.groupby(['year', 'Classificacao'], as_index=True).agg({'goals_difference': 'sum'})
    
    grouped_by_year = grouped_by_year.reset_index() 
    #print(grouped_by_year.head())
    
    for classificacao in grouped_by_year['Classificacao'].unique():#seleciona classificacao unica
        df_filtrado = grouped_by_year[grouped_by_year['Classificacao'] == classificacao]#cria uma "label"
        plt.plot(df_filtrado['year'], df_filtrado['goals_difference'], marker='o', label=classificacao)#adiciona uma "linha"
    plt.xlabel("Ano")
    plt.ylabel("Saldo")
    plt.legend(title="Classificação")  
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('graficos/saldosporano.png')
    plt.clf() 
