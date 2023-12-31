import numpy as np
import matplotlib.pyplot as plt

from custom_poling.core.target import Target
from custom_poling.core.custom_crystal import CustomCrystal

# Crystal properties
domain_width = 10.0e-6
number_domains = 1000
L = number_domains * domain_width
k0 = np.pi / domain_width

# Numerical integration parameters
k_range = 100/L
dk = k_range/401
k_array = np.arange(k0-k_range/2,k0+k_range/2,dk)

# Create a custom crystal object
custom_crystal_gauss = CustomCrystal(domain_width,number_domains)
domain_middles_gauss = custom_crystal_gauss.domain_middles

# Define and plot a Gaussian target function
std = 10/L
height = 0.00025
target_pmf_gauss = lambda k:1j*height*np.exp(-(k-k0)**2/(2*std**2))*np.exp(1j * L/2 * k)
target_gauss = Target(target_pmf_gauss,k_array)
target_gauss.plot_pmf(show=False, save_as="target_pmf_gauss.pdf")

# Compute and plot the target amplitude
target_amplitude_gauss = target_gauss.compute_amplitude(k0,domain_middles_gauss)
target_gauss.plot_amplitude(show=False, save_as="target_amplitude_gauss.pdf")

# Compute and plot the custom domains
custom_domains_gauss = custom_crystal_gauss.compute_domains(target_amplitude_gauss,k0)
custom_crystal_gauss.plot_domains(show=False, save_as="custom_domains_gauss.pdf")

# Compute and plot the PMF for the cystomized crystal
custom_crystal_gauss.compute_pmf(k_array)

# Compare the output PMF to the target PMF
plt.plot(k_array,np.abs(target_gauss.pmf),label='Target PMF')
plt.plot(k_array,np.abs(custom_crystal_gauss.pmf),label='Custom PMF')
plt.legend()
plt.savefig("compare_PMF.pdf")
print("Saved figure as: compare_PMF.pdf")

# Compute amplitudes
custom_amplitude,z_list= custom_crystal_gauss.compute_amplitude(k0,num_internal_points=1)

# Compare the output amplitudes to the target amplitudes
plt.plot(z_list,np.abs(custom_amplitude),label='Custom amplitude')
plt.plot(custom_crystal_gauss.domain_middles,np.abs(target_gauss.amplitude),label='Target amplitude')
plt.legend()
plt.savefig("compare_amplitudes.pdf")
print("Saved figure as: compare_amplitudes.pdf")