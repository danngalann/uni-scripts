import sys

class Grafo():
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for columna in range(vertices)]
                      for fila in range(vertices)]
        self.padre = [None] * self.V

    def imprimir_MST(self):
        print("Arista \tPeso")
        for i in range(1, self.V):
            print(self.padre[i], "-", i, "\t", self.grafo[i][self.padre[i]])

    def get_aristas(self):
        aristas = []
        for i in range(1, self.V):
            aristas.append((self.padre[i], i))
        return aristas
    
    def get_costes(self):
        costes = []
        for i in range(1, self.V):
            costes.append(self.grafo[i][self.padre[i]])
        return costes

    def clave_minima(self, camino, visitado, i):

        minimo = sys.maxsize

        for v in range(self.V):
            if camino[v] < minimo and visitado[v] == False:
                minimo = camino[v]
                indice_minimo = v

        return indice_minimo

    def prim_MST(self):

        camino = [sys.maxsize] * self.V
        

        camino[0] = 0
        visitado = [False] * self.V

        self.padre[0] = -1

        for i in range(self.V):
            u = self.clave_minima(camino, visitado, i)

            visitado[u] = True

            for v in range(self.V):
                if self.grafo[u][v] > 0 and visitado[v] == False \
                        and camino[v] > self.grafo[u][v]:
                    camino[v] = self.grafo[u][v]
                    self.padre[v] = u