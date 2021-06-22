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
        # self.amplitudes = amplitudes
        return self.domain_configuration

    def compute_pmf(self, k_array): 
        self.pmf = super().compute_pmf(self.domain_configuration,k_array)
        return self.pmf

    def plot_domains(self,n_max=None): 
        super().plot_domains(self.domain_configuration,n_max)

    def compute_amplitude(self,k,num_internal_points=0):
        amplitude_one_domain = lambda z1,z2:2*np.pi*1j*(np.exp(-1j*k*z2)-np.exp(-1j*k*z1))/(2*np.pi*k)
        amplitude = 0
        self.amplitudes = [0]
        z = self.z0
        z_array = [self.z0]
        for idx in range(len(self.domain_configuration)):
            domain_width = (self.domain_walls[idx+1]-self.domain_walls[idx])
            delta_z = domain_width/(num_internal_points+1)
            amplitudes_in = []
            for point in np.arange(1,num_internal_points+1):
                z = self.domain_walls[idx]+point*delta_z
                amplitudes_in = amplitudes_in + [amplitude + self.domain_configuration[idx]*amplitude_one_domain(self.domain_walls[idx],z)]
                z_array = z_array + [z] 
            amplitude = amplitude + self.domain_configuration[idx]*amplitude_one_domain(self.domain_walls[idx],self.domain_walls[idx+1])
            self.amplitudes = self.amplitudes + amplitudes_in + [amplitude]
            z_array = z_array + [self.domain_walls[idx+1]] 
        return self.amplitudes,z_array