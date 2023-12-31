import numpy as np
import matplotlib.pyplot as plt

class Target:

    def __init__(self,pmf_func,k_array):
        self.pmf_func = pmf_func
        self.k_array = k_array
        self.pmf = self.pmf_func(k_array)

    def plot_pmf(self,show=True,save_as=False,fix_ticks=False):
        """Plots the taret phasematching function (PMF).
        
        Returns:
            Plot of PMF as a function of k_array
        """
        plt.plot(self.k_array,np.abs(self.pmf),label='abs')
        plt.plot(self.k_array,np.real(self.pmf),'--',label='real')
        plt.plot(self.k_array,np.imag(self.pmf),'--',label='imag')
        plt.xlabel(r'$\Delta k$')
        plt.ylabel('Target PMF')
        plt.legend()
        if fix_ticks==True:
            plt.xticks(rotation=45)
        if type(save_as)==str:
            plt.savefig(save_as)
            plt.close()
            print("Saved figure as: " + save_as)
        if show==False:
            plt.close()
        if show:
            plt.show()

    def compute_amplitude(self,k,z_array,z0=0):
        """Computes the target amplitude.
        
        Returns:
            The target amplitude as a function of z_array.
        """
        self.k = k
        self.z_array = z_array
        self.z0 = z0
        amplitude = []
        for z1 in self.z_array:
            phase = lambda k1,k2,za,z0a: 1j*(np.exp(-1j*(k1-k2)*za)-np.exp(-1j*(k1-k2)*z0a))/(k1-k2)
            phase_factor = phase(self.k_array,self.k,z1,self.z0)
            self.dk = self.k_array[1]-self.k_array[0]
            kernel = self.pmf * phase_factor
            result = np.sum(kernel) * self.dk
            amplitude = amplitude + [result]
        self.amplitude = np.array(amplitude)/(2*np.pi)
        return self.amplitude

    def plot_amplitude(self,show=True,save_as=False,fix_ticks=False):
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
        if fix_ticks==True:
            plt.xticks(rotation=45)
        if type(save_as)==str:
            plt.savefig(save_as)
            plt.close()
            print("Saved figure as: " + save_as)
        if show==False:
            plt.close()
        if show:
            plt.show()

