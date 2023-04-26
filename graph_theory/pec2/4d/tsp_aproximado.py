from Grafo import Grafo

def coste(v1, v2):
    coste = 0
    for i in range(len(v1)):
        coste_color = abs(v1[i] - v2[i])

        if coste_color > coste:
            coste = coste_color
    
    return coste

# Paso 1: Generar matriz del grafo
A = [0,0,0]
B = [2,2,7]
C = [3,3,3]
D = [0,0,0]
E = [1,1,1]
F = [0,0,0]
G = [1,1,1]
H = [2,2,7]
I = [0,0,0]
J = [1,1,1]
K = [2,2,7]
L = [0,0,0]
M = [1,1,1]
N = [2,2,7]
O = [3,3,3]

v = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O]
n_vertices = len(v)

matriz = [[0 for i in range(n_vertices)] for j in range(n_vertices)]

for i in range(n_vertices):
    for j in range(n_vertices):
        matriz[i][j] = coste(v[i], v[j])

print('Matriz:')
for row in matriz:
    print(", ".join([str(col) for col in row]))

# Paso 2: Encontrar MST con Prim y almazenar las aristas
arbol_generador = Grafo(n_vertices)
arbol_generador.grafo = matriz
arbol_generador.prim_MST()

aristas = arbol_generador.get_aristas()
costes = arbol_generador.get_costes()
coste_total = sum(costes)
print(f"aristas: {aristas}")
print(f"costes: {costes}")
print(f"coste_total: {coste_total}")

# Paso 3: Genera la matriz con el arból generador
matriz_arbol = [[0 for i in range(n_vertices)] for j in range(n_vertices)]

for i in range(n_vertices):
    for j in range(n_vertices):
        if (i,j) in aristas:
            matriz_arbol[i][j] = matriz[i][j]

print('Matriz arbol:')
for row in matriz_arbol:
    print(", ".join([str(col) for col in row]))