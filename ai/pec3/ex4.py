def t_norm(a, b):
    return min(a, b)

def t_conorm(a, b):
    return max(a, b)

def membership_level(x, a, b, c, d):
    return max(min((x-a)/(b-a) if b-a != 0 else 1, 1, (d-x)/(d-c) if d-c != 0 else 1), 0)

def yager_complement(a, w=1):
    return (1 - a**w)**(1/w)

def get_degree(var_term):
    if var_term.startswith('NOT_'):
        negated_term = var_term[4:]  # Extract the term after 'NOT_'
        var_degree = globals().get(f'var{negated_term}', 0)
        return yager_complement(var_degree)
    else:
        return globals().get(f'var{var_term}', 0)

varA_value = 6
varC_value = 1.1

varA_L = membership_level(varA_value, 0, 0, 0, 7)
varA_M = membership_level(varA_value, 0, 7, 7, 8)
varA_H = membership_level(varA_value, 6, 8, 8, 10)
varA_VH = membership_level(varA_value, 8, 10, 10, 10)

varC_VL = membership_level(varC_value, 0, 0, 0.2, 0.6)
varC_L = membership_level(varC_value, 0, 0.4, 0.6, 1.4)
varC_M = membership_level(varC_value, 0.8, 1.0, 1.0, 1.2)
varC_H = membership_level(varC_value, 0.6, 1.4, 1.6, 2.0)
varC_VH = membership_level(varC_value, 1.4, 1.8, 2.0, 2.0)

rules_outB3 = {
    1: ('L', 'L', 'AND', 'VL'),
    2: ('L', 'L', 'AND', 'L'),
    3: ('L', 'M', 'AND', 'M'),
    4: ('L', 'H', 'AND', 'H'),
    5: ('L', 'VH', 'AND', 'H'),
    6: ('L', 'NOT_VL', 'AND', 'H'),
    7: ('L', 'NOT_L', 'AND', 'H'),
    8: ('L', 'NOT_M', 'AND', 'M'),
    9: ('L', 'NOT_H', 'AND', 'L'),
    10: ('L', 'NOT_VH', 'AND', 'VL'),
    11: ('M', 'VL', 'AND', 'L'),
    12: ('M', 'L', 'AND', 'L'),
    13: ('M', 'M', 'AND', 'M'),
    14: ('M', 'H', 'AND', 'H'),
    15: ('M', 'VH', 'AND', 'H')
}

print("Evaluación de las reglas para OutB3:")
rule_outputs_outB3 = {}
for i, (varA_term, varC_term, condition, outB3_term) in rules_outB3.items():
    varA_degree = globals().get(f'varA_{varA_term}', 0) if varA_term else 1
    varC_degree = globals().get(f'varC_{varC_term}', 0) if varC_term else 1

    if condition == 'AND':
        rule_degree = t_norm(varA_degree, varC_degree)
    elif condition == 'OR':
        rule_degree = t_conorm(varA_degree, varC_degree)

    rule_outputs_outB3[i] = rule_degree
    rule_status = "activada" if rule_degree > 0 else "no activada"
    print(f"Regla {i}: {rule_status} con un grado de {rule_degree}")

output_terms_outB3 = {
    'VL': 0,
    'L': 0,
    'M': 0,
    'H': 0,
    'VH': 0
}
for i, degree in rule_outputs_outB3.items():
    output_term = rules_outB3[i][3]
    output_terms_outB3[output_term] = max(output_terms_outB3[output_term], degree)

print("\nSalida final agregada para OutB3:")
print(output_terms_outB3)

