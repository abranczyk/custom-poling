import numpy as np
import matplotlib.pyplot as plt

from custom_poling.utils.pmf import pmf

class Crystal:
    """ A class for a poled crystal.
    
    Attr:
        domain_width
        number_domains
        z0
        length = domain_width * number_domains
        domain_walls
        domain_middles
    """

    def __init__(self, domain_width, number_domains, z0=0):
        """ Initialize the Crystal class.
        
        Params:
            domain_width
            number_domains
        """
        self.domain_width = domain_width
        self.number_domains = number_domains
        self.z0 = z0
        self.length = self.number_domains * self.domain_width
        self.domain_walls = np.arange(z0, z0 + (self.number_domains + 1) * self.domain_width, self.domain_width)
        self.domain_middles = (self.domain_walls + self.domain_width/2)[0:-1]
    
    def compute_pmf(self, domain_configuration, k_array):
        """Returns the phasematching function (PMF) as a function of k for a given domain_configuration.

        Args:
            domain_configuration (list of int): elements of list must be +1 or -1
            k_array (array of floats)

        Returns:
            PMF as an array of floats
        """
        self.domain_configuration = domain_configuration
        self.k_array = k_array
        crystal_pmf = pmf(self.domain_walls, self.domain_configuration, self.k_array)
        return crystal_pmf

    def plot_domains(self,domain_configuration,n_max=None,show=True,save_as=False,fix_ticks=False):
        x_axis = self.domain_walls
        y_axis = np.concatenate(([domain_configuration[0]],domain_configuration))
        if n_max != None and n_max < len(x_axis):
            x_axis = x_axis[0:n_max]
            y_axis = y_axis[0:n_max]
        plt.step(x_axis,y_axis)
        plt.xlabel('z')
        plt.ylabel('g(z)')
        plt.ylim([-1.2, 1.2])
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
