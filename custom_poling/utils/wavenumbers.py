import numpy as np

from custom_poling.utils.sellmeier import Sellmeier

class Wavenumbers:
    def __init__(self,A1,A2,A3,A4):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.c = 3e8
        self.conversion = 1e6
        self.x = lambda omega: 2*np.pi*self.c*self.conversion/omega
        self.k = lambda omega: omega * np.sqrt(self.A1 + self.A2/(self.x(omega)**2 - self.A3) - self.A4 * self.x(omega)**2)/self.c
        self.k1 = lambda omega: (self.A1*(self.x(omega)**2-self.A3)**2 + self.A2*(2*self.x(omega)**2-self.A3))/(self.c*(self.x(omega)**2-self.A3)**2*np.sqrt(self.A1+self.A2/(self.x(omega)**2-self.A3)-self.x(omega)**2*self.A4))
        self.k2 = lambda omega: (self.x(omega)**3*(self.A2*(-self.A2*(2*self.x(omega)**2+self.A3)+self.A1*(-3*self.x(omega)**4+2*self.x(omega)**2*self.A3+self.A3**2))+(self.x(omega)**2-self.A3)*(self.A1*(self.x(omega)**2-self.A3)**3+self.A2*(6*self.x(omega)**4-3*self.x(omega)**2*self.A3+self.A3**2))*self.A4))/(2*self.c**2*self.conversion*np.pi*(self.x(omega)**2-self.A3)**3*np.sqrt(self.A1+self.A2/(self.x(omega)**2-self.A3)-self.x(omega)**2*self.A4)*(-self.A2+(self.x(omega)**2-self.A3)*(-self.A1+self.x(omega)**2*self.A4)))