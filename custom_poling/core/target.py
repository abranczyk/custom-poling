import numpy as np
import matplotlib.pyplot as plt

from amplitude_function import AmplitudeFunction

class Target:

    def __init__(self,pmf_func,k_array):
        self.pmf_func = pmf_func
        self.k_array = k_array
        self.pmf = self.pmf_func(k_array)

    def plot_pmf(self):
        """Plots the taret phasematching function (PMF).
        
        Returns:
            Plot of PMF as a function of k_array
        """
        plt.plot(self.k_array,np.abs(self.pmf),label='abs')
        plt.plot(self.k_array,np.real(self.pmf),'--',label='real')
        plt.plot(self.k_array,np.imag(self.pmf),'--',label='imag')
        plt.xlabel('Delta k')
        plt.ylabel('Target PMF')
        plt.legend()
        plt.show()

    def compute_amplitude(self,k,z_array,dz,z0=0):
        """Computes the target amplitude.
        
        Returns:
            The target amplitude as a function of z_array.
        """
        self.k = k
        self.z_array = z_array
        self.dz = dz
        self.z0 = z0
        amplitude = []
        for z1 in self.z_array:
            amplitude = amplitude + [AmplitudeFunction(self.pmf,self.k_array,k,z1,dz,z0).compute()]
        self.amplitude = np.array(amplitude)/(2*np.pi)
        return self.amplitude

    def plot_amplitude(self):
        """Plots the taret phasematching function (PMF).
        
        Returns:
            Plot of PMF as a function of k_array
        """
        plt.plot(self.z_array,np.abs(self.amplitude),'x',label='abs')
        plt.plot(self.z_array,np.real(self.amplitude),'.',label='real')
        plt.plot(self.z_array,np.imag(self.amplitude),'.',label='imag')
        plt.xlabel('z')
        plt.ylabel('Target Amplitude')
        plt.legend()
        plt.show()