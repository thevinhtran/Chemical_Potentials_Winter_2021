""" Module that defines particle classes and provides initial list of baryons, leptons, mesons 
    Hopefully would allow for ease of use of declaring particles
"""

import numpy as np
import pandas as pd
import sympy as sym


class eos:
    # equation of state class
    # can use to declare an EOS object that contains the coupling constants for the model 

    def __init__(self, g_sigma_N = 0.0, g_omega_N = 0.0, g_rho_N = 0.0, g_phi_N = 0.0, b = 0.0, c = 0.0,\
                    g_sigma_H = 0.0, g_omega_H = 0.0, g_rho_H = 0.0, g_phi_H = 0.0):
        
        self.g_sigma_N = g_sigma_N
        self.g_omega_N = g_omega_N
        self.g_rho_N = g_rho_N
        self.g_phi_N = g_phi_N
        
        self.g_sigma_H = g_sigma_H
        self.g_omega_H = g_omega_H
        self.g_rho_H = g_rho_H
        self.g_phi_H = g_phi_H
        
        self.b = b
        self.c = c

        # mixed coupling
        # self.g_sigma_omega... 
        # self.g_sigma_rho... 
        # self.g_omega_rho... etc, etc 


class baryon:
    # baryon class
    # use to declare a baryon object that holds attributes of that particle such as mass, charge, etc 
    def __init__(self, ):

        self.


class lepton: 
    def __init__(self, ):
        self. 


class meson: 
    def __init__(self, ):
        self. 


Neutron = [sym.symbols('m_n'), sym.symbols('n_n'), sym.symbols('n_B')*sym.symbols('x_n'), sym.symbols('x_n'), sym.symbols('mu_n'), 0.0]
Proton = [sym.symbols('m_p'), sym.symbols('n_p'), sym.symbols('n_B')*sym.symbols('x_p'), sym.symbols('x_p'), sym.symbols('mu_p'), 1.0]
Lambda_0 = [sym.symbols('n_Lambda_0'), sym.symbols('n_B')*sym.symbols('x_Lambda_0'), sym.symbols('x_Lambda_0'),\
             sym.symbols('mu_Lambda_0'),  0.0]
Sigma_0 = [sym.symbols('n_Sigma_0'), sym.symbols('n_B')*sym.symbols('x_Sigma_0'), sym.symbols('x_Sigma_0'),\
           sym.symbols('mu_Sigma_0'), 0.0]
Sigma_neg = [sym.symbols('n_Sigma_-'), sym.symbols('n_B')*sym.symbols('x_Sigma_-'), sym.symbols('x_Sigma_-'),\
           sym.symbols('mu_Sigma_-'), 0.0]
Cascade_neg = [sym.symbols('n_\Xi_-'), sym.symbols('n_B')*sym.symbols('x_\Xi-'), sym.symbols('x_\Xi-'),\
               sym.symbols('mu_\Xi_-'), -1.0]




# MESONS 

Sigma = 
Omega = 
Rho = 
Phi = 


