import matplotlib.pyplot as plt

def pizza_dist(formato_atual):
    valores = []
    classificados = formato_atual[formato_atual['season'] ==  2006]

    classificados = classificados['Classificacao'].value_counts()
    #print(classificados.values)
    valores = list(classificados.values)
    #print(valores)
    plt.pie(valores, labels=classificados.index, startangle=140, autopct='%1.1f%%')
    plt.axis('equal')  
    plt.savefig('graficos/distribuicaodevagas.png')
