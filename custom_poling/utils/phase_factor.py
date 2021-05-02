import numpy as np

class PhaseFactor:

    def __init__(self,k1,k2,z,dz,z0=0):
        self.k1 = k1
        self.k2 = k2
        self.z = z
        self.dz = dz
        self.z_array = np.arange(z0, self.z + self.dz, self.dz)

    def compute(self):
        kernel = np.exp(-1j * (self.k1 - self.k2) * self.z_array)
        return np.sum(kernel) * self.dz
