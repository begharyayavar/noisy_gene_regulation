import random
from defaults import *

class Noise:
    def __init__(   self,\
                        noise_type :str = default_noise_type,\
                        noise_mu : float = default_noise_mu,\
                        noise_sigma : float = default_noise_sigma,\
                        noise_coefficient : float = default_noise_coefficient):
        self.type = noise_type
        self.mu = noise_mu
        self.sigma = noise_sigma
        self.coefficient = noise_coefficient
    
    def generate(self) -> float:
        if self.type == "None":
            return 0
        elif self.type == "Gaussian":
            return random.gauss(self.mu,self.sigma)
    
    def get_type(self) -> str:
        return self.type
    def get_mu(self) -> float:
        return self.mu
    def get_sigma(self) -> float:
        return self.sigma
    def get_coefficient(self) -> float:
        return self.coefficient
    
    def __repr__(self) -> str:
        return "Noise:\n\
            Type: {}\n\
            Mu: {}\n\
            Sigma: {}\n\
            Coefficient: {}\n".\
            format(self.type,self.mu,self.sigma,self.coefficient)            