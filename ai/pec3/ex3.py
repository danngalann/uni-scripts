# Funciones para t-norma y t-conorma
def t_norm(a, b):
    return min(a, b)

def t_conorm(a, b):
    return max(a, b)

# Función trapezoidal
def trapezoidal(x, a, b, c, d):
    return max(min((x-a)/(b-a) if b-a != 0 else 1, 1, (d-x)/(d-c) if d-c != 0 else 1), 0)

# Función de la familia Yager para el conjunto complementario
def yager_complement(a, w=1):
    return (1 - a**w)**(1/w)

# Valores de entrada
varC_value = 1.1
varD_value = 1.25

# Grados de pertenencia para VarC y VarD
varC_VL = trapezoidal(varC_value, 0, 0, 0.2, 0.6)
varC_L = trapezoidal(varC_value, 0, 0.4, 0.6, 1.4)
varC_M = trapezoidal(varC_value, 0.8, 1.0, 1.0, 1.2)
varC_H = trapezoidal(varC_value, 0.6, 1.4, 1.6, 2.0)
varC_VH = trapezoidal(varC_value, 1.4, 1.8, 2.0, 2.0)

varD_L = trapezoidal(varD_value, 0, 0, 0, 1)
varD_M = trapezoidal(varD_value, 0, 1, 1, 2)
varD_H = trapezoidal(varD_value, 0, 1, 2, 2)

# Reglas para OutB2
rules_outB2 = {
    1: ('VL', 'L', 'AND'),
    2: ('VL', 'M', 'AND'),
    3: ('VL', 'H', 'AND'),
    4: ('L', 'L', 'AND'),
    5: ('L', 'M', 'AND'),
    6: ('L', 'H', 'AND'),
    7: ('M', 'L', 'AND'),
    8: ('M', 'M', 'AND'),
    9: ('M', 'H', 'AND'),
    10: ('H', 'L', 'AND'),
    11: ('H', 'M', 'AND'),
    12: ('H', 'H', 'AND'),
    13: ('VH', 'L', 'AND'),
    14: ('VH', 'M', 'AND'),
    15: ('VH', 'H', 'AND')
}

# Evaluación de las reglas
print("Evaluación de las reglas para OutB2:")
rule_outputs_outB2 = {}
for i, (varC_term, varD_term, condition) in rules_outB2.items():
    varC_degree = globals().get(f'varC_{varC_term}', 0)
    varD_degree = globals().get(f'varD_{varD_term}', 0)
    varD_complement = yager_complement(varD_degree) # Aplicación del complemento Yager

    # Aplicar t-norma
    rule_degree = t_norm(varC_degree, varD_complement)
    rule_outputs_outB2[i] = rule_degree
    rule_status = "activada" if rule_degree > 0 else "no activada"
    print(f"Regla {i}: {rule_status} con un grado de {rule_degree}")

# Agregación de las salidas de las reglas
output_terms_outB2 = {
    'VL': 0,
    'L': 0,
    'M': 0,
    'H': 0,
    'VH': 0
}
for i, degree in rule_outputs_outB2.items():
    output_term = rules_outB2[i][1] # Término de salida de la regla
    output_terms_outB2[output_term] = max(output_terms_outB2[output_term], degree)

print("\nSalida final agregada para OutB2:")
print(output_terms_outB2)

