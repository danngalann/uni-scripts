from sklearn.tree import DecisionTreeClassifier, export_text, export_graphviz
from graphviz import Source
import pandas as pd

# Crear el conjunto de datos
data = {
    'Size': ['S', 'S', 'B', 'B', 'S', 'S', 'B', 'B', 'S', 'S', 'S', 'B', 'B', 'S', 'B', 'B'],
    'Distance': ['N', 'N', 'N', 'N', 'F', 'F', 'F', 'F', 'N', 'N', 'F', 'N', 'N', 'F', 'F', 'F'],
    'Humidity': ['M', 'L', 'M', 'H', 'H', 'L', 'H', 'L', 'L', 'M', 'L', 'M', 'H', 'L', 'L', 'M'],
    'Test': ['Y', 'Y', 'Y', 'N', 'Y', 'N', 'N', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'N', 'N', 'Y']
}
df = pd.DataFrame(data)

# Convertir datos categóricos a numéricos
df_encoded = pd.get_dummies(df, columns=['Size', 'Distance', 'Humidity'])

# Separar las características y el objetivo
X = df_encoded.drop('Test', axis=1)
y = df_encoded['Test']

# Crear y entrenar el árbol de decisión
decision_tree = DecisionTreeClassifier(criterion='entropy', random_state=0)
decision_tree.fit(X, y)

# Exportar el árbol en formato de texto
tree_rules = export_text(decision_tree, feature_names=list(X.columns))
print(tree_rules)

# Guardar el árbol en formato PNG
tree = Source(export_graphviz(decision_tree, feature_names=list(X.columns), class_names=['N', 'Y'], filled=True, out_file=None))
png_bytes = tree.pipe(format='png')
with open('tree.png','wb') as f:
    f.write(png_bytes)