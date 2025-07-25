import pandas as pd
import numpy as np
from isotope_data_v4 import isotopes  # your isotope dictionary
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Load cross-section CSV files
absorption_df = pd.read_csv('Absorption_Cross_Section_Data.csv')
capture_df = pd.read_csv('Capture_Cross_Section_Data.csv')
n2n_df = pd.read_csv('n2n_Cross_Section_Data.csv')

# Load flux (175-group), assuming it's a single-column file
flux = np.loadtxt('Flux.txt')
flux = flux.flatten()

# Normalize flux if necessary
if flux.sum() > 0:
    flux = flux / flux.sum()

# Compute group-averaged cross-sections
def average_cross_sections(df, flux):
    avg_xs = {}
    for isotope in df.columns:
        xs = df[isotope].values
        avg_xs[isotope] = np.sum(xs * flux)
    return avg_xs

avg_cross_sections = {
    'absorption': average_cross_sections(absorption_df, flux),
    'capture': average_cross_sections(capture_df, flux),
    'n2n': average_cross_sections(n2n_df, flux)
}

# Update isotope dictionary with averaged cross-sections
for iso in isotopes:
    isotopes[iso]['n_gamma'] = avg_cross_sections['capture'].get(iso, 0.0)
    isotopes[iso]['n_2n'] = avg_cross_sections['n2n'].get(iso, 0.0)
    isotopes[iso]['n_fission'] = avg_cross_sections['absorption'].get(iso, 0.0)

# Build the list and mapping for ODEs
isotope_list = list(isotopes.keys())
index_map = {iso: i for i, iso in enumerate(isotope_list)}

# Load initial materials (no header)
materials_df = pd.read_csv('Materials.txt', delim_whitespace=True, header=None)
N0 = np.zeros(len(isotope_list))
for _, row in materials_df.iterrows():
    iso = row[0]
    amount = row[1]
    if iso in index_map:
        N0[index_map[iso]] = amount
    else:
        print(f"Warning: Isotope '{iso}' not found in isotope dictionary.")

# Define ODE system
def odes(t, y):
    dydt = np.zeros_like(y)
    for iso, props in isotopes.items():
        i = index_map[iso]
        loss = (props['n_gamma'] + props['n_2n'] + props['n_fission']) * y[i] + props['decay'] * y[i]
        prod = 0.0
        for parent, reaction in props['prod']:
            j = index_map[parent]
            if reaction == 'n_gamma':
                prod += isotopes[parent]['n_gamma'] * y[j]
            elif reaction == 'n_2n':
                prod += isotopes[parent]['n_2n'] * y[j]
            elif reaction == 'n_fission':
                prod += isotopes[parent]['n_fission'] * y[j]
            elif reaction == 'decay':
                prod += isotopes[parent]['decay'] * y[j]
        dydt[i] = prod - loss
    return dydt

# Simulation time setup
years = float(input("Enter burnup duration in years (e.g., 10): "))
T_end = years * 365.25 * 24 * 3600
t_eval = np.linspace(0, T_end, 1000)

# Solve
sol = solve_ivp(odes, [0, T_end], N0, t_eval=t_eval, method='BDF')
'''
# Plot results
plt.figure(figsize=(12, 7))
for i, iso in enumerate(isotope_list):
    plt.plot(sol.t / (365.25 * 24 * 3600), sol.y[i], label=iso)
plt.xlabel('Time (years)')
plt.ylabel('Relative Concentration')
plt.title('Isotope Production in U-238 Burnup Chain')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
'''
# Final concentrations
for i, iso in enumerate(isotope_list):
    print(f"{iso}: {sol.y[i][-1]:.4e}")
