def t_norm(a, b):
    return min(a, b)

def t_conorm(a, b):
    return max(a, b)

def membership_level(x, a, b, c, d):
    return max(min((x-a)/(b-a) if b-a != 0 else 1, 1, (d-x)/(d-c) if d-c != 0 else 1), 0)

def yager_complement(a, w=1):
    return (1 - a**w)**(1/w)

varC_value = 1.1
varD_value = 1.25

varC_VL = membership_level(varC_value, 0, 0, 0.2, 0.6)
varC_L = membership_level(varC_value, 0, 0.4, 0.6, 1.4)
varC_M = membership_level(varC_value, 0.8, 1.0, 1.0, 1.2)
varC_H = membership_level(varC_value, 0.6, 1.4, 1.6, 2.0)
varC_VH = membership_level(varC_value, 1.4, 1.8, 2.0, 2.0)

varD_L = membership_level(varD_value, 0, 0, 0, 1)
varD_M = membership_level(varD_value, 0, 1, 1, 2)
varD_H = membership_level(varD_value, 0, 1, 2, 2)

rules_outB2 = {
    1: ('VL', 'L', 'AND', 'VL'),
    2: ('VL', 'M', 'AND', 'VL'),
    3: ('VL', 'H', 'AND', 'L'),
    4: ('L', 'L', 'AND', 'L'),
    5: ('L', 'M', 'AND', 'L'),
    6: ('L', 'H', 'AND', 'M'),
    7: ('M', 'L', 'AND', 'M'),
    8: ('M', 'M', 'AND', 'M'),
    9: ('M', 'H', 'AND', 'M'),
    10: ('H', 'L', 'AND', 'M'),
    11: ('H', 'M', 'AND', 'H'),
    12: ('H', 'H', 'AND', 'H'),
    13: ('VH', 'L', 'AND', 'H'),
    14: ('VH', 'M', 'AND', 'VH'),
    15: ('VH', 'H', 'AND', 'VH')
}

print("Evaluación de las reglas para OutB2:")
rule_outputs_outB2 = {}
for i, (varC_term, varD_term, condition, outB2_term) in rules_outB2.items():
    varC_degree = globals().get(f'varC_{varC_term}', 0) if varC_term else 1
    varD_degree = globals().get(f'varD_{varD_term}', 0) if varD_term else 1

    if condition == 'AND':
        rule_degree = t_norm(varC_degree, varD_degree)
    elif condition == 'OR':
        rule_degree = t_conorm(varC_degree, varD_degree)
    elif condition == 'NOT_A':
        not_varC_degree = yager_complement(varC_degree)
        rule_degree = not_varC_degree
    elif condition == 'NOT_B':
        not_varD_degree = yager_complement(varD_degree)
        rule_degree = not_varD_degree
    elif condition == 'NOT_BOTH_OR':
        not_varC_degree = yager_complement(varC_degree)
        not_varD_degree = yager_complement(varD_degree)
        rule_degree = t_conorm(not_varC_degree, not_varD_degree)
    elif condition == 'NOT_BOTH_AND':
        not_varC_degree = yager_complement(varC_degree)
        not_varD_degree = yager_complement(varD_degree)
        rule_degree = t_norm(not_varC_degree, not_varD_degree)

    rule_outputs_outB2[i] = rule_degree
    rule_status = "activada" if rule_degree > 0 else "no activada"
    print(f"Regla {i}: {rule_status} con un grado de {rule_degree}")

output_terms_outB2 = {
    'VL': 0,
    'L': 0,
    'M': 0,
    'H': 0,
    'VH': 0
}
for i, degree in rule_outputs_outB2.items():
    output_term = rules_outB2[i][3]
    output_terms_outB2[output_term] = max(output_terms_outB2[output_term], degree)

print("\nSalida final agregada para OutB2:")
print(output_terms_outB2)

