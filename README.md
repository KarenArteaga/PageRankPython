# Algoritmo Page Rank para Python
> Implementación del algoritmo Page Rank de Google en Python
---
Proyecto final de la materia Cálculo Numérico
Creado por:
- Karen Artega Mendoza 190161
- Eduardo Riveros Mckay Aguilera 174724

---
Mayo 2022

## Tabla de contenidos
* [Introducción](#info)
* [Simulación de las páginas web de Google](#simula)
* [Implementación](#implem)
* [Pruebas](#pruebas)
* [Conclusiones](#conclusiones)
* [Referencias](#referencias)


## Introducción <a name="info"></a> 

PageRank (PR) es un algoritmo utilizado por Google Search para clasificar sitios web en los resultados de su motor de búsqueda. PageRank lleva el nombre de Larry Page, uno de los fundadores de Google. PageRank es una forma de medir la importancia de las páginas de un sitio web. 

PageRank funciona contando el número y la calidad de los enlaces a una página para determinar una estimación aproximada de la importancia del sitio web. La suposición diría que es probable que los sitios web más importantes reciban más enlaces de otros sitios web.

No es el único algoritmo utilizado por Google para ordenar los resultados del motor de búsqueda, pero es el primer algoritmo que utilizó la empresa, y es el más conocido.
La medida de centralidad anterior no se implementa para gráficos múltiples.

Algoritmo
El algoritmo PageRank genera una distribución de probabilidad que se utiliza para representar la probabilidad de que una persona que hace clic aleatoriamente en los enlaces llegue a una página en particular. PageRank se puede calcular para colecciones de documentos de cualquier tamaño. Se supone en varios trabajos de investigación que la distribución se divide uniformemente entre todos los documentos de la colección al comienzo del proceso computacional. Los cálculos de PageRank requieren varias pasadas, llamadas "iteraciones", a través de la colección para ajustar los valores aproximados de PageRank para reflejar más fielmente el valor real teórico.



## Simulación de las páginas web de Google <a name="simula"></a> 
En abril 2022, se estima que Google tiene alrededor de 200.5 millones de sitios web activos. Esto se traduce a cientos de millones de páginas web y, como resultado, miles de millones de hipervínculos entre paginas web. Este sistema de páginas e hipervínculos se puede representar como un grafo dirigido de cientos de millones de nodos que almacenan las páginas web y miles de millones de aristas que representan los hipervículos entre páginas. Sin embargo, simular un sistema con una cantidad tan elevada de elementos y conexiones es innecesario, pues la implementación del algoritmo es la misma para conjuntos de cardinalidad mínima. Por lo tanto, para fines prácticos, se decidió representar el conjunto de páginas web de Google con un grafo dirigido de una cantidad mínima de nodos (10 - 100) y una probabilidad de aristas de 0.6 aleatorias.

## Implementación <a name="implem"></a> 
La implementación del algoritmo Page Rank se realizó en el lenguage Python y se puede replicar duplicando este repositorio. 
Los pasos que se siguieron para la implementación son:
1. Crear un grafo dirigido aleatorio con n nodos y probabilidad de aristas p.
2. Crear un diccionario vacío para el ranking.
3. Seleccionar un nodo aleatorio del grafo.
4. Asignar un valor de cero a cada nodo del grafo.
5. Sumar 1 al valor del nodo selccionado.
6. Crear una lista de vecinos del nodo seleccionado.
7. Si la lista es vacía, seleccionar un nuevo nodo aleatorio del grafo y sumar 1 a su valor.
8. Si la lista no es vacía, seleccionar un nodo aleatorio de la lista y sumar 1 a su valor.
9. Iterar 600000 veces los pasos 6-8.
10. Normalizar los valores dividiendo entre el número de iteraciones.
11. Imprimir los nodos en orden descendente según el valor asignado

## Pruebas y resultados
Se utilizó la función `pagerank` del paquete NetworkX de Python para comparar los resultados del algoritmo implementado. La función `pagerank` de Networkx computa el ranking de los nodos de una grafo G basado en la estructura de las aristas:
  
  `networkx.pagerank(G, P)`,

donde:
- G: grafo que se va a utilizar
- P: probabilidad de generar una arista

Después se ordenó el diccionario de nodos en orden decreciente según el valor asignado por la función `pagerank`. Finalmente, se imprimió el diccionario ordenado para compararlo con el diccionario resultante de la implementación del algoritmo.  

### Resultados
  Se hicieron 3 pruebas del algoritmo para diferentes grafos.
  
  1. Grafo con 10 nodos y probabilidad de generar arista de 0.6
    ![gr1](https://user-images.githubusercontent.com/69361149/169181775-1aa9ada1-ca22-4678-bd1c-5ad0dfe5132d.png)
    ![r1](https://user-images.githubusercontent.com/69361149/169181855-92880b65-0212-4cab-9a00-b1e8dc9d03a0.png)

    
  2. Grafo con 25 nodos y probabilidad de generar arista de 0.6
    ![gr2](https://user-images.githubusercontent.com/69361149/169181887-d4e93219-c4d9-4978-a6e2-8d95d3ee35ce.png)
    ![r2](https://user-images.githubusercontent.com/69361149/169181924-1f52cd3f-2d99-4e8d-a9d8-13b7fea4f579.png)


  3. Grafo con 50 nodos y probabilidad de generar arista de 0.6
    ![gr3](https://user-images.githubusercontent.com/69361149/169181956-856355aa-83cf-48a5-b840-d3736886c6c2.png)
    ![r3](https://user-images.githubusercontent.com/69361149/169181995-14a80551-add0-4be0-bac9-ebcbd583b39e.png)


## Conclusiones


## Referencias 
https://www.semrush.com/blog/pagerank/?kw=&cmp=LM_SRCH_DSA_Blog_Core_BU_EN&label=dsa_pagefeed&Network=g&Device=c&utm_content=515715498615&kwid=dsa-1057183199035&cmpid=11799892963&agpid=112575465737&BU=Core&extid=23624544571&adpos=&gclid=CjwKCAjwj42UBhAAEiwACIhADsOhj5NanvnwMsCDatEAOIJF4yHDsivQZVgmDvAeOaax9I5OUnLkohoCWcIQAvD_BwE

https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html

https://siteefy.com/how-many-websites-are-there/#How-Many-Webpages-Are-There

https://medium.com/analytics-vidhya/how-google-search-works-page-rank-algorithm-using-python-9643d9c9a981
