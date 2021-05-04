import numpy as np

class PhaseFactor:

    def __init__(self,k1,k2,z,dz,z0=0):
        self.k1 = k1
        self.k2 = k2
        self.z = z
        self.z0 = z0

    def compute(self):
        return 1j*(np.exp(-1j*(self.k1-self.k2)*self.z)-np.exp(-1j*(self.k1-self.k2)*self.z0))/(self.k1-self.k2)
