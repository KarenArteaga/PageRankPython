# Algoritmo Page Rank para Python
> Implementación del algoritmo Page Rank de Google en Python
---
Proyecto final de la materia Cálculo Numérico
Creado por:
- Karen Artega Mendoza 190161
- Eduardo Riveros 

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


## Simulación de las páginas web de Google <a name="simula"></a> 
En abril 2022, se estima que Google tiene alrededor de 200.5 millones de sitios web activos. Esto se traduce a cientos de millones de páginas web y, como resultado, miles de millones de hipervínculos entre paginas web. Este sistema de páginas e hipervínculos se puede representar como un grafo dirigido de cientos de millones de nodos que almacenan las páginas web y miles de millones de aristas que representan los hipervículos entre páginas. Sin embargo, simular un sistema con una cantidad tan elevada de elementos y conexiones es innecesario, pues la implementación del algoritmo es la misma para conjuntos de cardinalidad mínima. Por lo tanto, para fines prácticos, se decidió representar el conjunto de páginas web de Google con un grafo dirigido de una cantidad mínima de nodos (10 - 100) y una probabilidad de aristas de 0.6 con pesos aleatorios.

## Implementación <a name="implem"></a> 
La implementación del algoritmo Page Rank se realizó en el lenguage Python. 
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

## Pruebas

## Conclusiones


## Referencias 
