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
varB_value = 5

varA_L = membership_level(varA_value, 0, 0, 0, 7)
varA_M = membership_level(varA_value, 0, 7, 7, 8)
varA_H = membership_level(varA_value, 6, 8, 8, 10)
varA_VH = membership_level(varA_value, 8, 10, 10, 10)

varB_L = membership_level(varB_value, 0, 0, 0, 4)
varB_M = membership_level(varB_value, 2, 3, 7, 8)
varB_H = membership_level(varB_value, 4, 8, 8, 9)

rules_outB1 = {
    1: ('L', 'L', 'OR', 'VL'),
    2: (None, 'NOT_L', 'AND', 'H'),
    3: ('M', 'L', 'AND', 'VH'),
    4: ('M', 'M', 'AND', 'M'),
    5: ('M', 'H', 'AND', 'VH'),
    6: ('NOT_H', None, 'AND', 'L'),
    7: ('NOT_VH', 'NOT_H', 'OR', 'L'),
    8: ('H', 'H', 'OR', 'VH'),
    9: ('VH', 'H', 'OR', 'VH')
}

print("Evaluación de las reglas:")
rule_outputs_outB1 = {}
for i, (varA_term, varB_term, condition, outB1_term) in rules_outB1.items():
    varA_degree = globals().get(f'varA_{varA_term}', 0) if varA_term else 1
    varB_degree = globals().get(f'varB_{varB_term}', 0) if varB_term else 1

    if condition == 'AND':
        rule_degree = t_norm(varA_degree, varB_degree)
    elif condition == 'OR':
        rule_degree = t_conorm(varA_degree, varB_degree)

    rule_outputs_outB1[i] = rule_degree
    rule_status = "activada" if rule_degree > 0 else "no activada"
    print(f"Regla {i}: {rule_status} con un grado de {rule_degree}")

output_terms_outB1 = {
    'VL': 0,
    'L': 0,
    'M': 0,
    'H': 0,
    'VH': 0
}
for i, degree in rule_outputs_outB1.items():
    output_term = rules_outB1[i][3]
    output_terms_outB1[output_term] = max(output_terms_outB1[output_term], degree)

print("\nSalida final agregada para OutB1:")
print(output_terms_outB1)
