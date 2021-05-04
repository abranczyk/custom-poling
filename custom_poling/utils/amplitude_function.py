import numpy as np

from custom_poling.utils.phase_factor import PhaseFactor

class AmplitudeFunction:

    def __init__(self,pmf,k_array,k,z,z0=0):
        self.pmf = pmf
        self.k_array = k_array
        self.k = k
        self.z = z
        self.z0 = z0

    def compute(self):
        phase_factor = []
        self.dk = self.k_array[1]-self.k_array[0]
        phase_factor = []
        for k1 in self.k_array:
            phase_factor += [PhaseFactor(k1,self.k,self.z,self.z0).compute()]
        phase_factor = np.array(phase_factor)
        kernel = self.pmf * phase_factor
        return np.sum(kernel) * self.dk