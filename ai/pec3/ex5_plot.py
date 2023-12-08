import matplotlib.pyplot as plt
import numpy as np

def membership_level(x, a, b, c, d):
    return max(min((x-a)/(b-a) if b-a != 0 else 1, 1, (d-x)/(d-c) if d-c != 0 else 1), 0)

membership_functions_outB4 = {
    'VL': lambda x: membership_level(x, 0, 0, 0, 1),
    'L': lambda x: membership_level(x, 0, 2, 2, 3),
    'M': lambda x: membership_level(x, 2, 4, 5, 6),
    'H': lambda x: membership_level(x, 5, 6, 6, 9),
    'VH': lambda x: membership_level(x, 7, 8, 10, 10)
}

output_terms_outB4 = {'VL': 0.14285714285714285, 'L': 0.49999999999999944, 'M': 0.8571428571428571, 'H': 0.6250000000000002, 'VH': 0.6250000000000002}

x_values = np.linspace(0, 10, 500)
aggregated_membership = np.zeros_like(x_values)

plt.figure(figsize=(10, 6))

for term, degree in output_terms_outB4.items():
    mf_values = np.array([membership_functions_outB4[term](x) for x in x_values])
    plt.plot(x_values, mf_values, label=f'{term} (Grado: {degree:.2f})', linestyle='--')
    aggregated_membership = np.fmax(aggregated_membership, np.fmin(degree, mf_values))

plt.plot(x_values, aggregated_membership, label='Salida agregada', color='black')
plt.title('Funciones de membresía de salida agregadas')
plt.xlabel('X')
plt.ylabel('Grado de membresía')
plt.legend()
plt.grid(True)
plt.show()
