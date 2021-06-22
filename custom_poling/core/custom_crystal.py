import numpy as np
import matplotlib.pyplot as plt

from custom_poling.core.crystal import Crystal
from custom_poling.utils.pmf import pmf

class CustomCrystal(Crystal):

    def __init__(self, domain_width, number_domains, z0=0):
        super().__init__(domain_width, number_domains, z0)

    def compute_domains(self,target_amplitudes,k):
        domain_configuration = []
        amplitudes = []
        for target_amplitude in target_amplitudes:
            ampPRE = pmf(self.domain_walls,domain_configuration, k)
            ampUP  = pmf(self.domain_walls,domain_configuration + [1], k)
            ampDW  = pmf(self.domain_walls,domain_configuration + [-1], k)
            test_amplitudes = np.array([np.mean([ampPRE, ampUP]), np.mean([ampPRE, ampDW])])
            cost = target_amplitude - test_amplitudes
            cost = np.abs(cost)
            if cost[0] == np.min(cost):
                domain_configuration = domain_configuration + [1]
                amplitudes = amplitudes + [test_amplitudes[0]]
            elif cost[1] == np.min(cost):
                domain_configuration = domain_configuration + [-1]
                amplitudes = amplitudes + [test_amplitudes[1]]
        self.domain_configuration = np.array(domain_configuration)
        self.amplitudes = amplitudes
        return self.domain_configuration

    def compute_pmf(self, k_array): 
        self.pmf = super().compute_pmf(self.domain_configuration,k_array)
        return self.pmf

    def plot_domains(self,n_max=None): 
        super().plot_domains(self.domain_configuration,n_max)

    def compute_amplitude(self,k):
        self.wall_amplitudes = []
        for z in self.domain_walls:
            self.wall_amplitudes = self.wall_amplitude + [pmf(self.domain_walls,self.domain_configuration, k)]
        return self.wall_amplitudes