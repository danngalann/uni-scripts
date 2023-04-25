# Programa de Python3 para comprobar si un grafo conectado es bipartito o no utilizando DFS

# Función para almacenar los nodos conectados
def addEdge(adj, u, v):

    adj[u].append(v)
    adj[v].append(u)

# Función para comprobar si un grafo es bipartito o no
def isBipartite(adj, v, visited, color):

    for u in adj[v]:

        # Si el vértice u no ha sido explorado antes
        if (visited[u] == False):

            # Marcar los vértices presentes como visitados
            visited[u] = True

            # Marcar su color opuesto al de su padre
            color[u] = not color[v]

            # Si el subárbol enraizado en el vértice v no es bipartito
            if (not isBipartite(adj, u,
                                visited, color)):
                return False

        # Si dos adyacentes están coloreados con el mismo color, entonces el grafo no es bipartito
        elif (color[u] == color[v]):
            return False

    return True

if __name__=='__main__':

    # Número de nodos
    N = 11

    # Para mantener la lista de adyacencia del grafo
    adj = [[] for i in range(N + 1)]

    # Para verificar si un nodo ha sido descubierto o no
    visited = [0 for i in range(N + 1)]

    # Para colorear los vértices del grafo con 2 colores
    color = [0 for i in range(N + 1)]

    # Agregar aristas al grafo
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)
    addEdge(adj, 4, 5)
    addEdge(adj, 5, 6)
    addEdge(adj, 6, 7)
    addEdge(adj, 7, 8)
    addEdge(adj, 8, 9)
    addEdge(adj, 9, 2)
    addEdge(adj, 6, 11)
    addEdge(adj, 10, 3)
    addEdge(adj, 10, 5)
    addEdge(adj, 10, 7)
    addEdge(adj, 10, 9)

    # Marcar el nodo de origen como visitado
    visited[1] = True

    # Marcar el nodo de origen con un color
    color[1] = 0

    # Función para comprobar si el grafo es bipartito o no
    if (isBipartite(adj, 1, visited, color)):
        print("El grafo es bipartito")
    else:
        print("El grafo no es bipartito")