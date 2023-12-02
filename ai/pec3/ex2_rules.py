# Funciones para t-norma y t-conorma
def t_norm(a, b):
    return min(a, b)

def t_conorm(a, b):
    return max(a, b)

# Reglas y sus condiciones con índice
rules_with_index = {
    1: ('L', 'L', 'OR'), # L OR L
    2: ('L', 'NOT_L', 'AND'), # L AND NOT(L)
    3: ('M', 'L', 'AND'), # M AND L
    4: ('M', 'M', 'AND'), # M AND M
    5: ('M', 'H', 'AND'), # M AND H
    6: ('NOT_H', 'ANY', 'NOT_A'), # NOT(H)
    7: ('NOT_VH', 'NOT_H', 'OR'), # NOT(VH) OR NOT(H)
    8: ('H', 'H', 'OR'), # H OR H
    9: ('VH', 'H', 'OR')  # VH OR H
}

# Grados de pertenencia específicos
varA_L = 0.857
varA_H = 0
varA_VH = 0
varB_L = 0
varB_M = 1
varB_H = 0.25
varB_NOT_L = 1 - varB_L

# Evaluación de las reglas con impresión de la evaluación
print("Evaluación de las reglas:")
rule_outputs = {}
for i, (varA_term, varB_term, condition) in rules_with_index.items():
    varA_degree = globals().get(f'varA_{varA_term}', 0)
    varB_degree = globals().get(f'varB_{varB_term}', 0)

    # Aplicar la condición adecuada
    if condition == 'AND':
        rule_degree = t_norm(varA_degree, varB_degree)
    elif condition == 'OR':
        rule_degree = t_conorm(varA_degree, varB_degree)
    elif condition == 'NOT_A':
        rule_degree = 1 - varA_degree
    elif condition == 'NOT_B':
        rule_degree = 1 - varB_degree

    rule_outputs[i] = rule_degree
    rule_status = "activada" if rule_degree > 0 else "no activada"
    print(f"Regla {i}: {rule_status} con un grado de {rule_degree}")

# Agregación de las salidas de las reglas
output_terms = {
    'VL': 0,
    'L': 0,
    'M': 0,
    'H': 0,
    'VH': 0
}
# Mapeo de cada regla a su término de salida correspondiente
rule_to_output_mapping = {
    1: 'VL', # Regla 1 afecta a VL
    2: 'H',  # Regla 2 afecta a H
    3: 'VH', # Regla 3 afecta a VH
    4: 'M',  # Regla 4 afecta a M
    5: 'VH', # Regla 5 afecta a VH
    6: 'L',  # Regla 6 afecta a L
    7: 'L',  # Regla 7 afecta a L
    8: 'VH', # Regla 8 afecta a VH
    9: 'VH'  # Regla 9 afecta a VH
}

# Agregación correcta: Tomar el máximo de los grados de activación de las reglas para cada término de salida
for i, degree in rule_outputs.items():
    output_term = rule_to_output_mapping.get(i)
    if output_term:
        output_terms[output_term] = max(output_terms[output_term], degree)

print("\nSalida final agregada para OutB1:")
print(output_terms)
