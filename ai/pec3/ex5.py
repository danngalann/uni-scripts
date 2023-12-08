import numpy as np

def t_norm(a, b, c):
    return min(a, b, c)

def t_conorm(a, b, c):
    return max(a, b, c)

def yager_complement(a, w=1):
    return (1 - a**w)**(1/w)

def membership_level(x, a, b, c, d):
    return max(min((x-a)/(b-a) if b-a != 0 else 1, 1, (d-x)/(d-c) if d-c != 0 else 1), 0)

def get_degree(var_term, values_dict):
    if var_term.startswith('NOT_'):
        negated_term = var_term[4:]  # Extract the term after 'NOT_'
        var_degree = values_dict.get(negated_term, 0)
        return yager_complement(var_degree)
    else:
        return values_dict.get(var_term, 0)
    
def calculate_center_of_mass(output_terms, membership_functions, resolution=100):
    x_values = np.linspace(0, 1, resolution)
    aggregated_membership = np.zeros_like(x_values)

    for term, degree in output_terms.items():
        mf = membership_functions[term]
        mf_values = np.array([mf(x) for x in x_values])
        aggregated_membership = np.fmax(aggregated_membership, np.fmin(degree, mf_values))

    numerator = np.sum(aggregated_membership * x_values)
    denominator = np.sum(aggregated_membership)

    if denominator == 0:
        return 0  # Evitar división por cero
    return numerator / denominator

def evaluate_rule(outB1_term, outB2_term, outB3_term, condition):
    degrees = [get_degree(term, values_dict) for term, values_dict in 
               zip([outB1_term, outB2_term, outB3_term], [out_B1, out_B2, out_B3]) 
               if term]

    if condition == 'AND':
        return t_norm(*degrees)
    elif condition == 'OR':
        return t_conorm(*degrees)

out_B1 = {'VL': 0.14285714285714285, 'L': 0, 'M': 0.8571428571428571, 'H': 0, 'VH': 0.25}
out_B2 = {'VL': 0, 'L': 0.37499999999999983, 'M': 0.49999999999999944, 'H': 0.6250000000000002, 'VH': 0}
out_B3 = {'VL': 0.14285714285714285, 'L': 0.37499999999999983, 'M': 0.49999999999999944, 'H': 0.6250000000000002, 'VH': 0}

rules_outB4 = {
    1: ('VL', 'VL', 'VL', 'AND', 'VL'),
    2: ('VL', '', 'VL', 'OR', 'VL'),
    3: ('VL', '', 'L', 'OR', 'L'),
    4: ('', 'VL', 'VL', 'OR', 'VL'),
    5: ('VL', '', 'M', 'OR', 'L'),
    6: ('L', 'L', 'L', 'AND', 'VL'),
    7: ('L', 'L', '', 'OR', 'L'),
    8: ('L', '', 'L', 'OR', 'L'),
    9: ('M', 'M', 'M', 'AND', 'M'),
    10: ('M', '', '', '', 'M'),
    11: ('M', '', 'M', 'OR', 'M'),
    12: ('', 'M', 'L', 'OR', 'M'),
    13: ('', 'M', 'L', 'OR', 'L'),
    14: ('', 'M', 'M', 'OR', 'M'),
    15: ('H', 'H', 'H', 'AND', 'H'),
    16: ('H', 'H', '', 'OR', 'H'),
    17: ('', 'H', 'H', 'OR', 'H'),
    18: ('', '', 'VH', '', 'VH'),
    19: ('VH', '', 'H', 'OR', 'VH'),
    20: ('', 'H', 'VH', 'OR', 'H'),
    21: ('VH', 'VH', 'VH', 'AND', 'VH')
}

print("Evaluación de las reglas para OutB4:")
rule_outputs_outB4 = {}
for i, (outB1_term, outB2_term, outB3_term, condition, outB4_term) in rules_outB4.items():
    outB1_degree = get_degree(outB1_term, out_B1)
    outB2_degree = get_degree(outB2_term, out_B2)
    outB3_degree = get_degree(outB3_term, out_B3)

    if condition == 'AND':
        rule_degree = t_norm(outB1_degree, outB2_degree, outB3_degree)
    elif condition == 'OR':
        rule_degree = t_conorm(outB1_degree, outB2_degree, outB3_degree)

    rule_outputs_outB4[i] = rule_degree
    rule_status = "activada" if rule_degree > 0 else "no activada"
    print(f"Regla {i}: {rule_status} con un grado de {rule_degree}")

output_terms_outB4 = {
    'VL': 0,
    'L': 0,
    'M': 0,
    'H': 0,
    'VH': 0
}
for i, degree in rule_outputs_outB4.items():
    output_term = rules_outB4[i][4]
    output_terms_outB4[output_term] = max(output_terms_outB4[output_term], degree)

print("\nSalida final agregada para OutB4:")
print(output_terms_outB4)

membership_functions_outB4 = {
    'VL': lambda x: membership_level(x, 0, 0, 0, 1),
    'L': lambda x: membership_level(x, 0, 2, 2, 3),
    'M': lambda x: membership_level(x, 2, 4, 5, 6),
    'H': lambda x: membership_level(x, 5, 6, 6, 9),
    'VH': lambda x: membership_level(x, 7, 8, 10, 10)
}

# Calcular el centro de masa
center_of_mass_outB4 = calculate_center_of_mass(output_terms_outB4, membership_functions_outB4)
print(f"Centro de masa: {center_of_mass_outB4}")