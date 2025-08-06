#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 11:06:33 2025

@author: anupam
"""

# U-cycle burnup model

import numpy as np
import pandas as pd
import os
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from junk.isotope_data_mod_v1 import isotopes

df_neutron_energy = pd.read_csv('Neutron_Energy_Groups.txt', sep='\t')
def load_cross_section_data(file_path):
    df = pd.read_csv(file_path,sep='\t')*1.0E-24 # barns to cm2
    return df.to_dict(orient='list')

# Load decay constants
decay_constant = pd.read_csv('Lambda.txt',sep='\t').to_dict('records')[0]

# Load cross-section data
absorption_data = load_cross_section_data('Absorption_Cross_Section_Data.txt')
capture_data = load_cross_section_data('Capture_Cross_Section_Data.txt')
n2n_data = load_cross_section_data('n2n_Cross_Section_Data.txt')

# Build a dictionary for each reaction type
absorption_data = {isotope: np.array(data) for isotope, data in absorption_data.items() if isotope in isotopes}
capture_data = {isotope: np.array(data) for isotope, data in capture_data.items() if isotope in isotopes}
n2n_data = {isotope: np.array(data) for isotope, data in n2n_data.items() if isotope in isotopes}

# Create a dictionary to hold all cross-section data
nuclear_data = {
    'absorption': absorption_data,
    'n_gamma': capture_data,
    'n2n': n2n_data,
    'decay': decay_constant
}

# Load the 175-group flux data
flux = pd.read_csv('Flux.txt', header=None).squeeze().values
flux_sum = np.sum(flux)
spectrum = flux[:]/flux_sum

# ask user to input the file name
input_file = input("Enter the input file name (e.g., 'Deplete_Problem3.inp'): ")  

with open(input_file, 'r') as f:
    # lines = [f.readline().strip() for _ in range(2)]
    lines = [line.strip() for line in f.readlines()]

for line in lines:
    if line.startswith('Isotopes'):
        isotope_names = [name.strip() for name in line.split(':')[1].strip().split(',')]
    elif line.startswith('Isotope masses'):
        isotope_masses = [float(m.strip()) for m in line.split(':')[1].strip().split(',')]
    if line.startswith('Time units'):
        time_unit = line.split(':')[1].strip()
    elif line.startswith('Time intervals'):
        time_intervals = list(map(float, line.split(':')[1].strip().split(',')))
    elif line.startswith('Time step'):
        time_step = list(map(float, line.split(':')[1].strip().split(',')))[0]
    elif line.startswith('Flux fractions'):
        flux_fractions = list(map(float, line.split(':')[1].strip().split(',')))
    elif line.startswith('Total flux'):
        total_flux = float(line.split(':')[1].strip())

# Build the materials DataFrame
materials_df = pd.DataFrame({
    'Isotopes': isotope_names,
    'Isotope masses (g)': isotope_masses
})

# Convert the materials DataFrame to a dictionary
materials = materials_df.set_index('Isotopes')['Isotope masses (g)'].to_dict()
print(materials)

#create a dictionary for molar masses for each isotope
molar_masses = {
    'U234': 234.0409521,
    'U235': 235.0439299,
    'U236': 236.045568,
    'U237': 237.0487304,
    'U238': 238.0507882,
    'U239': 239.0542933,
    'Np236': 236.04657,
    'Np237': 237.0481734,
    'Np238': 238.0509466,
    'Np239': 239.052939,
    'Pu238': 238.0495599,
    'Pu239': 239.0521634,
    'Pu240': 240.0538135,
    'Pu241': 241.0568515,
    'Pu242': 242.0587428,
    'Pu243': 243.0613811,
    'Am241': 241.0568293,
    'Am242': 242.0595492,
    'Am243': 243.0613811
}

#convert Isotope masses to concentrations using molar masses

for isotope, mass in materials.items():
    if isotope in molar_masses:
        # Calculate concentration in atoms per cm^3
        concentration = (mass / molar_masses[isotope]) * 6.022e23
        materials[isotope] = concentration
    else:
        print(f"Warning: Molar mass for {isotope} not found.")
        
# Print the materials dictionary to verify concentrations
print("Materials concentrations (atoms/cm^3):", materials)

# Convert time intervals to seconds based on the time unit
if time_unit == 'd':
    time_intervals = np.array([t * 24 * 3600 for t in time_intervals])  # days to seconds
    time_step *= 24 * 3600
elif time_unit == 'y':
    time_intervals = np.array([t * 365.25 * 24 * 3600 for t in time_intervals])
    time_step *= 365.25 * 24 * 3600
elif time_unit == 's':
    time_intervals = np.array([t for t in time_intervals])
elif time_unit == 'h':
    time_intervals = np.array([t * 3600 for t in time_intervals])
    time_step *= 3600
elif time_unit == 'min':
    time_intervals = np.array([t * 60 for t in time_intervals])
    time_step *= 60
else:
    raise ValueError(f"Unsupported time unit: {time_unit}")

times = time_intervals.cumsum()
times = np.insert(times, 0, 0.0)
t_eval = {}
for i in range(len(time_intervals)):
    t_eval[f'Interval {i+1:d}'] = np.arange(times[i],times[i+1],time_step)
t_eval[list(t_eval.keys())[-1]] = np.append(t_eval[list(t_eval.keys())[-1]], times[-1])

interval_fluxes = (spectrum*total_flux).reshape(spectrum.shape[0],1)*np.array([flux_fractions])

#Convert cross secton data frrame to dict of arrays for quick lookup
def cross_section_lookup(isotope, reaction_type, group=1):
    """
    Lookup cross-section value for a given isotope, reaction type, and energy group.
    """
    if reaction_type in nuclear_data:
        if isotope in nuclear_data[reaction_type]:
            return nuclear_data[reaction_type][isotope][group-1]
    

#build isotope list and idex list
isotope_list = list(isotopes.keys())
index_map = {iso: i for i, iso in enumerate(isotope_list)}

#intial conditions from amterial file
N0 = np.zeros(shape=(len(isotope_list),1))
for index, row in materials_df.iterrows():
    iso = row['Isotopes']
    amount = materials[iso]  # Use concentration in atoms/cm^3 from the materials dictionary
    print(f"Processing isotope: {iso}, concentration: {amount}")
    if iso in index_map:
        N0[index_map[iso],0] = amount
    else:
        print(f"Warning: Isotope '{iso}' not found in the isotope model.")

def odes(t, y, evaluation_flux):
    """
    ODE system for burnup model using effective cross sections.
    y: vector of concentrations for each isotope.
    """
    dNdt = np.zeros_like(y)
    for i, iso in enumerate(isotope_list):
        production = isotopes[iso]['prod']
        depletion = isotopes[iso]['loss']
        
        gain = 0.0
        loss = 0.0
        
        for iso, rxn in production:
            if rxn == 'decay':
                gain += nuclear_data[rxn][iso]*y[index_map[iso]]
            else:
                gain += (nuclear_data[rxn][iso]*evaluation_flux).sum()*y[index_map[iso]]
        
        for iso, rxn in depletion:
            if rxn == 'decay':
                loss += nuclear_data[rxn][iso]*y[index_map[iso]]
            else:
                loss += (nuclear_data[rxn][iso]*evaluation_flux).sum()*y[index_map[iso]]
        
        dNdt[i] = gain-loss
    
    return dNdt
 
#solve the ODE system using solve_ivp
sol = None  # Initialize sol to None for later checks

print("Running the burnup model...")

N = np.zeros_like(N0)
t = np.concatenate(list(t_eval.values()))

for i in range(len(time_intervals)):
    evaluation_times = t_eval[f'Interval {i+1:d}']
    evaluation_flux = interval_fluxes[:,i]
    
    sol = solve_ivp(fun = odes, 
                    t_span = [0.0,evaluation_times[-1]], 
                    y0 = N0[:,-1], 
                    t_eval = evaluation_times,
                    method = 'BDF',
                    args=(evaluation_flux,)
                    )
    
    N0 = np.abs(sol.y)
    N = np.append(N,N0,axis=1)

N = np.delete(N, 0, axis=1)
result_dict = {iso: (N[index_map[iso],:]/6.022E+23)*molar_masses[iso] for iso in isotope_list}
"""
plot_list = ['U239']
#final concentrations of all isotopes
for iso in isotope_list:
    if iso not in plot_list:
        plot_list.append(iso)
# Print final concentrations
for iso in plot_list:
    print(f"{iso}: {result_dict[iso][-1]:.4f} g")
    

#Create a csv file to store the results, column 1 is time in d, rest of the colums are each isotopes and their subiquent masses 
output_df = pd.DataFrame({'Time (d)': t/86400.0})
for iso in plot_list:
    output_df[iso] = result_dict[iso]
output_df.to_csv('U238_Burnup_Results.csv', index=False)
print("Results saved to 'U238_Burnup_Results.csv'.")

    
# Plot the results
plt.figure(figsize=(12, 6))
for i, iso in enumerate(plot_list):
    plt.plot(t/86400.0, result_dict[iso], label=iso)
plt.xlabel('Time (s)')
plt.ylabel('Mass (g)')
plt.title('Isotope Masses Over Time')
plt.xscale('linear')
plt.yscale('linear')
plt.legend()
plt.grid()
plt.show()
    

"""

#plot only U235 and no other isotopes
#ask user to input the isotopes to plot
plot_list = input("Enter the isotopes to plot (comma-separated, e.g., 'U235,U238'): ").strip().split(',')
plot_list = [iso.strip() for iso in plot_list if iso.strip() in result_dict]  # Filter valid isotopes

# Print final concentrations

    #plot the results
#plot where y axis is mass in grams from scale 0-700
for iso in plot_list:
    print(f"{iso}: {result_dict[iso][-1]:.4f} g")
plt.figure(figsize=(12, 6))
for i, iso in enumerate(plot_list):
    plt.plot(t/86400.0, result_dict[iso], label=iso)
plt.xlim(0, max(t/86400.0))  # Set x-axis limit to the maximum time in days
plt.ylim(0, 700)  # Set y-axis limit to 0-700 grams
plt.xlabel('Time (d)')
plt.ylabel('Mass (g)')
plt.title('Isotope Masses Over Time')
plt.xscale('linear')
plt.yscale('linear')
plt.legend()
plt.grid()
plt.show()

# Save only the results for U235 to a CSV file
output_df = pd.DataFrame({
    'Time (d)': t/86400.0,
    plot_list[0]: result_dict[plot_list[0]]
})
output_df.to_csv(plot_list[0] + '_Burnup_Results.csv', index=False)
print(f"Results saved to '{plot_list[0]}_Burnup_Results.csv'.")