import numpy as np
from pmf import pmf
import matplotlib.pyplot as plt
from crystal import Crystal

class CustomCrystal(Crystal):

    def __init__(self, domain_width, number_domains, z0=0):
        super().__init__(domain_width, number_domains, z0)

    def compute_domains(self,target_amplitudes,k):
        domain_configuration = []
        for target_amplitude in target_amplitudes:
            ampPRE = pmf(self.domain_walls,domain_configuration, k)
            ampUP  = pmf(self.domain_walls,domain_configuration + [1], k)
            ampDW  = pmf(self.domain_walls,domain_configuration + [-1], k)
            amplitudes = np.array([np.mean([ampPRE, ampUP]), np.mean([ampPRE, ampDW])])
            cost = target_amplitude - amplitudes
            cost = np.abs(cost)
            if cost[0] == np.min(cost):
                domain_configuration = domain_configuration + [1]
            elif cost[1] == np.min(cost):
                domain_configuration = domain_configuration + [-1]
        self.domain_configuration = np.array(domain_configuration)
        return self.domain_configuration

    def compute_pmf(self, k_array): 
        self.pmf = super().compute_pmf(self.domain_configuration,k_array)
        return self.pmf

    # def plot_pmf(self, domain_configuration, k_array):
    #     """Plots the phasematching function (PMF) as a function of k for a given domain_configuration.

    #     Args:
    #         domain_configuration (list of int): elements of list must be +1 or -1
    #         k_array (array of floats)

    #     Returns:
    #         Plot of PMF as a function of k_array
    #     """
    #     pmf = self.pmf(domain_configuration, k_array)
    #     plt.plot(k_array,np.abs(pmf),label='abs')
    #     plt.plot(k_array,np.real(pmf),'--',label='real')
    #     plt.plot(k_array,np.imag(pmf),'--',label='imag')
    #     plt.xlabel('Delta k')
    #     plt.ylabel('PMF')
    #     plt.legend()
    #     plt.show()