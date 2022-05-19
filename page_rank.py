
"""
Created on Tue May 17 11:15:32 2022

@author: karenarteaga
"""

import networkx as nx
import matplotlib.pyplot as plt
import random as rd
import pandas as pd

def dic_comprobacion(grafo):
    # Usar el Page Rank de networkx
    lista = nx.pagerank(grafo)

    # ordenar los nodos
    paginas_ordenadas = sorted(lista.items(),key = lambda v: [v[1], v[0]], reverse = True)
    return paginas_ordenadas

# generar un dataframe para los resultados
def resultados(mi_ranking, netw_ranking):
    # agregar datos obtenidos
    df1 = pd.DataFrame(mi_ranking, columns = ['     Nuestro', 'ranking    '])
    # agregar datos de Networkx
    df2 = pd.DataFrame(netw_ranking)
    df1['     NetworkX'] = df2[0]
    df1['ranking     '] = df2[1]
    df1.loc[-1] = ['Nodo', 'Valores', 'Nodo', 'Valores']
    df1.index = df1.index + 1  
    df1.sort_index(inplace = True) 
    df1.style
    print(df1)


def page_rank(num_nodos, prob):
    # Crear un grafo dirigido
    grafo = nx.gnp_random_graph(num_nodos, prob, directed = True)
    nx.draw(grafo, with_labels = True, font_color ='white', font_size = 12, node_color = 'blue')
    
    # Mostrar el grafo
    plt.show()
    
    # Algoritmo Page Rank
    ranking_dic = {}
    x = rd.randint(0, num_nodos - 1)
    
    for j in range(0, num_nodos):
      ranking_dic[j] = 0
    
    ranking_dic[x] = ranking_dic[x] + 1
    
    for i in range(600000):
      list_n = list(grafo.neighbors(x))
      if(len(list_n) == 0):
        x = rd.randint(0, num_nodos - 1)
        ranking_dic[x] = ranking_dic[x] + 1
      else:
        x = rd.choice(list_n)
        ranking_dic[x] = ranking_dic[x] + 1
     
    
    # Normalizar valores
    for j in range(0, num_nodos):
      ranking_dic[j] = ranking_dic[j]/600000
    
    
    # Ordenar los nodos por puntaje
    mi_ranking = sorted(ranking_dic.items(), key = lambda v: [v[1], v[0]], reverse = True)
    
    # generar ranking de Networkx
    netw_ranking = dic_comprobacion(grafo)
    
    # mostrar resultados
    resultados(mi_ranking, netw_ranking)
    

# resultados para grafo con 10 nodos
page_rank(10, 0.6)

# resultados para grafo con 25 nodos
page_rank(25, 0.6)

# resultados para grafo con 50 nodos
page_rank(50, 0.6)
