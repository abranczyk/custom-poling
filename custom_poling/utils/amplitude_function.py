import numpy as np

class AmplitudeFunction:
    """ A class for the amplitude function."""

    def __init__(self,pmf,k_array,k,z,z0=0):
        """ Initialize the class.
        
        Args:
            pmf [array]: The pmf evaluated as a function of k_array
            k_array [array]: An array over k (used to evaluate phase factor)
            k [flt]: Value of k at which the ampitude function is evaluated
            z [flt]: Value of z at which the amplitude funciton is evaluated
            z0 [flt]: Start of the crystal.
        """
        self.pmf = pmf
        self.k_array = k_array
        self.k = k
        self.z = z
        self.z0 = z0

    def compute(self):
        """ Computes the amplitude for a given k at position z. """
        phase = lambda k1,k2,za,z0a: 1j*(np.exp(-1j*(k1-k2)*za)-np.exp(-1j*(k1-k2)*z0a))/(k1-k2)
        phase_factor = phase(self.k_array,self.k,self.z,self.z0)
        self.dk = self.k_array[1]-self.k_array[0]
        kernel = self.pmf * phase_factor
        self.result = np.sum(kernel) * self.dk
        return self.result