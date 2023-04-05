import random

N = 10 #Siendo N el numero de Nodos

P = 0.2 # Siendo P la probabilidad de conexión de los nodos

# Inicializar la matriz vacia de adyacencia
matriz = [[0 for x in range(N)] for y in range(N)]

# Se genera la red aleatoria
for i in range(N):
    for j in range(i+1, N):
        if random.random() < P:
            matriz[i][j] = 1
            matriz[j][i] = 1
            
 # Ahora se imprime la mztriz completa
for fila in matriz:
    print(fila)
 

#Este script utiliza dos ciclos for para recorrer cada par de nodos en la red. Utiliza la función random del módulo homonimo para generar un número aleatorio entre 0 y 1. Si este número es menor que la probabilidad P especificada, se crea una conexión entre los dos nodos.
