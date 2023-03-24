#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def jonswap(Hs, Tp, df, fcutoff_high):
#     Inputs:
#         Hs: significant wave height
#         Tp: peak spectral period
#         df: frequency interval
#         fcutoff_high: high cutoff frequency

#     Outputs:
#         Sfjs: JONSWA spectrum as a function of frequency
#         Swjs: JONSWAP spectrum as a function of angular frequency
#         f: frequency
#         omega: angular frequency
    gamma = 3.3
    inv2pi = 0.15915494
    omega = np.arange(df/inv2pi, fcutoff_high/inv2pi + df, df/inv2pi)
    f = inv2pi*omega
    fp = 1/Tp
    fpOvrf4 = (fp/f)**4
    C = 1-0.287*np.log(gamma)
    
    alphalist = []
    for i in range(len(f)):
        if f[i] <= fp:
            sigma = 0.07
        if f[i] > fp:
            sigma = 0.09
        al = np.exp((-0.5*(((f[i]*Tp)-1.0)/sigma)**2))
        alphalist.append(al)
    
    alpha = np.array(alphalist)
    Swjs = inv2pi*C*(0.3125*Hs*Hs*fpOvrf4/f)*np.exp((-1.25*fpOvrf4))*(gamma**alpha)
    Sfjs = 2*np.pi*Swjs
    return Sfjs, Swjs, f, omega

