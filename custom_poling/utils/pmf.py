import numpy as np

def pmf(domain_walls, domain_configuration, k_array):
    """Returns the phasematching function (PMF) as a function of k for a given domain_configuration."""
    if np.any(k_array==0.):
        raise ValueError('all k_array elements must be non-zero')
    pmf_one_domain = lambda z1,z2:2*np.pi*1j*(np.exp(1j*k_array*z1)-np.exp(1j*k_array*z2))/(k_array*2*np.pi)
    pmf = 0
    for idx in range(len(domain_configuration)):
        pmf = pmf + domain_configuration[idx]*pmf_one_domain(domain_walls[idx],domain_walls[idx+1])
    return pmf