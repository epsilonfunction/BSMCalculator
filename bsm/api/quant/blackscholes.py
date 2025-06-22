

import numpy as np
from scipy.stats import norm
import unittest

class blackscholes:

    def __init__(self,
                 S:float = 490, 
                 K:float = 500,
                 r:float = 0.03,
                 t:float = 1/365,
                 q:float = 0.01,
                 sigma:float = 0.1):
        self.S = S
        self.K = K
        self.r = r
        self.t = t
        self.q = q
        self.sigma = sigma

        self.F = None

    def get_variables(self):
        return self.S, self.K, self.r, self.t, self.q, self.sigma        
    
    
    def get_F_approx(self):
        self.F = self.S* np.exp(
            (self.r-self.q) * self.t
        )

        return self.F

    def get_d1_76(self):

        if self.F == None:
            self.get_F_approx()

        self.d1_76 = (
            np.log(
                self.F/self.K
            ) + 0.5*self.sigma**2*self.t
        ) / (self.sigma*np.sqrt(self.t))
        
        return self.d1_76
    
    def get_d2_76(self):
        
        self.get_d1_76()
        self.d2_76 = self.d1_76 - self.sigma*(np.sqrt(self.t))

        return self.d2_76            
        
    def Call(self) -> float:

        self.get_d2_76()

        self.C = np.exp(-self.r * self.t) * (norm.cdf(self.d1_76) * self.F - norm.cdf(self.d2_76) * self.K)
        return self.C
    
    # @property #getter
    def Put(self) -> int:
        self.get_d2_76()
        self.P = np.exp(-self.r * self.t) * (norm.cdf(-self.d2_76) * self.K - norm.cdf(-self.d1_76) * self.F)
        return self.P
    
    def get_Greeks(self):

        return self.get_delta()
    
    def get_delta(self):

        self.C_delta = np.exp(-self.r*self.t) * norm.cdf(self.d1_76)
        self.P_delta = -np.exp(-self.r*self.t) * norm.cdf(-self.d1_76)

        return self.C_delta,self.P_delta 
    
    def get_gamma(self):

        self.Gamma = np.exp(-self.r*self.t) * norm.pdf(self.d1_76) / (self.F * self.sigma * np.sqrt(self.t))

        return self.Gamma    

if __name__ == "__main__":

    S = 550
    X = 555
    r = 0.03
    t = 1/365
    q = 0.01
    sigma = 0.1

    bs = blackscholes(S, X, r, t, q, sigma)
    
    print("Call Price:", round(bs.Call(),3))
    print("Put Price:", round(bs.Put(),3))