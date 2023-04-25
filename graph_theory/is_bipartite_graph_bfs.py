class Graph():

	def __init__(self, V):
		self.V = V
		self.graph = [[0 for column in range(V)] \
								for row in range(V)]

	# Esta función devuelve verdadero si el grafo G[V][V]
    # es bipartito, sino devuelve falso
	def isBipartite(self, src):

		# Crea un array de color para almacenar los colores
        # asignados a todos los vértices. El número del vértice
        # se utiliza como índice en este array.
        # El valor '-1' de colorArr[i] se utiliza para
        # indicar que no se ha asignado ningún color al
        # vértice 'i'. El valor 1 se utiliza para indicar
        # que se ha asignado el primer color y el valor 0
        # indica que se ha asignado el segundo color.
		colorArr = [-1] * self.V

		# Asigna el primer color a la fuente
		colorArr[src] = 1

		# Crea una cola (FIFO) de números de vértices y
	    # encola el vértice fuente para el recorrido BFS
		queue = []
		queue.append(src)

		# Ejecuta mientras haya vértices en la cola
	    # (similar a BFS)
		while queue:

			u = queue.pop()

			# Devuelve falso si hay un bucle propio
			if self.graph[u][u] == 1:
				return False

			for v in range(self.V):

				# Existe una arista de u a v y el destino
			    # v no tiene ningún color asignado
				if self.graph[u][v] == 1 and colorArr[v] == -1:

					# Asigna un color alternativo a este
				    # v adyacente de u
					colorArr[v] = 1 - colorArr[u]
					queue.append(v)

                # Existe una arista de u a v y el destino
			    # v tiene el mismo color que u
				elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
					return False

		# Si llegamos aquí, entonces todos los vértices adyacentes
		# se pueden colorear con un color alternativo
		return True

g = Graph(4)
g.graph = [[0, 1, 0, 1],
			[1, 0, 1, 0],
			[0, 1, 0, 1],
			[1, 0, 1, 0]
			]
			
print ("Yes" if g.isBipartite(0) else "No")