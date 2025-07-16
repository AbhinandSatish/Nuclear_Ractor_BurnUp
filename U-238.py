import numpy as np
import json
from scipy.integrate import solve_ivp
import pandas as pd

# Load isotope data from external JSON file
with open('isotope_data.json', 'r') as f:
    isotope_data = json.load(f)

# Recursively build the reaction chain starting from a given isotope
def build_isotope_chain(start, data):
    isotopes = {}
    visited = set()
    to_visit = [start]
    chain_representation = []

    while to_visit:
        parent = to_visit.pop()
        if parent in visited or parent not in data:
            continue
        visited.add(parent)

        entry = data[parent]
        decay = np.log(2) / entry['half_life'] if entry['half_life'] > 0 else 0.0
        n_gamma = entry.get('n_gamma', 0.0)

        isotopes[parent] = {
            'decay': decay,
            'n_gamma': n_gamma,
            'prod': []
        }

        for child, mode in entry.get('products', []):
            to_visit.append(child)
            if child not in isotopes:
                isotopes[child] = {'decay': 0.0, 'n_gamma': 0.0, 'prod': []}
            isotopes[child]['prod'].append((parent, mode))
            chain_representation.append(f"{parent} --{mode}--> {child}")

    return isotopes, chain_representation

# Build dynamic isotope network from U-238
start_isotope = 'U238'
isotopes, chain_log = build_isotope_chain(start_isotope, isotope_data)
phi = 1e14  # neutron flux [n/cm^2/s]
isotope_list = list(isotopes.keys())
index_map = {iso: i for i, iso in enumerate(isotope_list)}

# Define the system of ODEs
def odes(t, y):
    dydt = np.zeros_like(y)
    for iso, props in isotopes.items():
        i = index_map[iso]
        loss = (props['n_gamma'] * phi + props['decay']) * y[i]
        prod = 0.0
        for parent, reaction in props['prod']:
            j = index_map[parent]
            if reaction == 'n_gamma':
                prod += isotopes[parent]['n_gamma'] * phi * y[j]
            elif reaction == 'decay':
                prod += isotopes[parent]['decay'] * y[j]
        dydt[i] = prod - loss
    return dydt

# Initial conditions (only starting isotope present initially)
N0 = np.zeros(len(isotope_list))
N0[index_map[start_isotope]] = 1.0

# Time span
T_end = 10 * 365.25 * 24 * 3600  # 10 years in seconds
t_eval = np.linspace(0, T_end, 1000)

# Solve the system
sol = solve_ivp(odes, [0, T_end], N0, t_eval=t_eval, method='BDF')

# Create results table
final_concentrations = {iso: sol.y[i][-1] for i, iso in enumerate(isotope_list)}
df = pd.DataFrame(final_concentrations.items(), columns=['Isotope', 'Final Concentration'])
df = df.sort_values(by='Final Concentration', ascending=False).reset_index(drop=True)

# Display chain and table
print("\nIsotope Transmutation-Decay Chain:")
for step in chain_log:
    print(step)

print("\nFinal Isotope Concentrations after 10 years:")
print(df.to_string(index=False))
