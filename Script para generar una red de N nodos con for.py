import random
# Cantidad de nodos en la red
N = 10

# Probabilidad de conexión entre cada par de nodos
P = 0.2

# Inicializar la red con una lista vacía
network = []

# Crear N nodos
for i in range(N):
    network.append([])
 
 # Conectar cada par de nodos con probabilidad P
for i in range(N):
     for j in range(i, N):
         if i != j:
             if random.random() < P:
                 network[i].append(j)
                 network[j].append(i)
 
 # Imprimir la red
 #En este script se usa la librería random para generar un numero aleatorio entre 0 y 1 y se compara con la probabilidad P, de ser menor se conecta los nodos, si no no se conecta.
 #La red se almacena en una lista de listas, donde cada sublista representa un nodo y contiene los índices de los nodos conectados a él. print(network)

print(network)
