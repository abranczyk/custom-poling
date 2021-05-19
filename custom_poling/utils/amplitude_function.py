import numpy as np

class AmplitudeFunction:

    def __init__(self,pmf,k_array,k,z,z0=0):
        self.pmf = pmf
        self.k_array = k_array
        self.k = k
        self.z = z
        self.z0 = z0

    def compute(self):
        phase = lambda k1,k2,za,z0a: 1j*(np.exp(-1j*(k1-k2)*za)-np.exp(-1j*(k1-k2)*z0a))/(k1-k2)
        phase_factor = phase(self.k_array,self.k,self.z,self.z0)
        self.dk = self.k_array[1]-self.k_array[0]
        kernel = self.pmf * phase_factor
        return np.sum(kernel) * self.dk