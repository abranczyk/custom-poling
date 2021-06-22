import numpy as np

def pmf(domain_walls, domain_configuration, k):
    pmf_one_domain = lambda z1,z2:2*np.pi*1j*(np.exp(-1j*k*z2)-np.exp(-1j*k*z1))/(k*2*np.pi)
    pmf = 0
    for idx in range(len(domain_configuration)):
        pmf = pmf + domain_configuration[idx]*pmf_one_domain(domain_walls[idx],domain_walls[idx+1])
    return pmf