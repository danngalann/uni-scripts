import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    # Find the least cost vertex not yet visited
    def minKey(self, path, visited, i):

        min = sys.maxsize

        for v in range(self.V):
            if path[v] < min and visited[v] == False:
                min = path[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph
    def primMST(self):

        # Key values used to pick minimum weight edge in cut
        path = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        path[0] = 0
        visited = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for i in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(path, visited, i)

            # Put the minimum distance vertex in
            # the shortest path tree
            visited[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):

                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and visited[v] == False \
                        and path[v] > self.graph[u][v]:
                    path[v] = self.graph[u][v]
                    parent[v] = u

        
        self.printMST(parent)
        print('Visitados: ' + ' '.join([str(i)
              for i in range(0, len(visited)) if i]))
        print(f"Costes recorrido mínimo: {' '.join([str(i) for i in path])}")
        print(f"Cost mínimo total: {sum(path)}")


if __name__ == '__main__':
    g = Graph(6)
    # Adjacency matrix
    g.graph = [
        [0, 3, 10, 1, 0, 0],
        [3, 0, 0, 2, 4, 0],
        [10, 0, 0, 9, 0, 8],
        [1, 2, 9, 0, 5, 7],
        [0, 4, 0, 5, 0, 6],
        [0, 0, 8, 7, 6, 0]
    ]

    g.primMST()
