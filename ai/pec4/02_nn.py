import numpy as np
from sklearn.metrics import confusion_matrix, f1_score

# Datos de entrada y clases esperadas
data = np.array([
    [4, 8, 2, 1],
    [7, 2, 7, 1],
    [0, 9, 7, 0],
    [1, 4, 1, 0],
    [1, 1, 1, 0],
    [2, 3, 2, 1],
    [6, 0, 1, 0],
    [6, 5, 2, 1],
    [0, 9, 3, 0],
    [8, 3, 1, 0],
    [0, 2, 3, 0],
    [4, 2, 2, 0],
    [3, 8, 3, 1],
    [0, 4, 8, 1],
    [9, 10, 3, 0],
    [7, 5, 2, 1],
    [1, 10, 2, 1],
    [9, 10, 9, 1]
])

# Pesos de las conexiones neuronales
weights = {
    'x0': {'h0': 1, 'h1': -0.5, 'h2': 0.5, 'h3': 1},
    'x1': {'h0': -1, 'h1': 1, 'h2': 1, 'h3': -0.5},
    'x2': {'h0': 1, 'h1': -0.5, 'h2': -0.25, 'h3': 1},
    'h': {'y': {'h0': -1, 'h1': -0.5, 'h2': 1, 'h3': -0.25}}
}

# Función de activación ReLU
def relu(x):
    return np.maximum(0, x)

# Función heaviside
def heaviside(x):
    return 1 if x > 0 else 0

# Función para calcular la salida de la red
def calculate_output(observation):
    x0, x1, x2 = observation[:3]

    # Calculo de la capa oculta
    h0 = relu(weights['x0']['h0'] * x0 + weights['x1']['h0'] * x1 + weights['x2']['h0'] * x2)
    h1 = relu(weights['x0']['h1'] * x0 + weights['x1']['h1'] * x1 + weights['x2']['h1'] * x2)
    h2 = relu(weights['x0']['h2'] * x0 + weights['x1']['h2'] * x1 + weights['x2']['h2'] * x2)
    h3 = relu(weights['x0']['h3'] * x0 + weights['x1']['h3'] * x1 + weights['x2']['h3'] * x2)

    # Calculo de la capa de salida
    y = heaviside(weights['h']['y']['h0'] * h0 + weights['h']['y']['h1'] * h1 + weights['h']['y']['h2'] * h2 + weights['h']['y']['h3'] * h3)

    return y

# Calcular la salida para cada observación
predicted_classes = [calculate_output(observation) for observation in data]

# Clases reales
real_classes = [obs[3] for obs in data]

# Calcular la matriz de confusión y la métrica F1
conf_matrix = confusion_matrix(real_classes, predicted_classes)
f1 = f1_score(real_classes, predicted_classes)

print('Matriz de confusión:')
print(conf_matrix)

print('Métrica F1:', f1)

