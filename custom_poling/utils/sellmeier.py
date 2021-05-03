import numpy as np

class Sellmeier:
    def __init__(self,A1,A2,A3,A4):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.n = lambda x: np.sqrt(A1 + A2/(x**2 - A3) - A4 * x**2)