#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ts = np.arange(0, 3600, 0.1) # time series
T = ts[2]-ts[1] # dt
fs = 1/T # sampling frequency

df = 1/ts.max()
fcutoff_high = fs/2 # high cutoff frequency
Hs = 11.17 # significant wave height
Tp = 8.52 # peak spectral period

def jonswap(Hs, Tp, df, fcutoff_high):
#     Inputs:
#         Hs: significant wave height
#         Tp: peak spectral period
#         df: frequency interval
#         fcutoff_high: high cutoff frequency

#     Outputs:
#         Sfjs: JONSWAP spectrum as a function of frequency
#         Swjs: JONSWAP spectrum as a function of angular frequency
#         f: frequency
#         omega: angular frequency
    gamma = 3.3
    inv2pi = 0.15915494
    omega = np.arange(df/inv2pi, fcutoff_high/inv2pi + df, df/inv2pi)
    f = inv2pi*omega
    fp = 1/Tp
    fpdiv = (fp/f)**4
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
    Swjs = inv2pi*C*(0.3125*Hs*Hs*fpdiv/f)*np.exp((-1.25*fpdiv))*(gamma**alpha)
    Sfjs = 2*np.pi*Swjs
    return Sfjs, Swjs, f, omega

Sfjs, Swjs, f, omega = jonswap(Hs, Tp, df, fcutoff_high)

# example plot of JONSWAP spectrum (in frequency domain)
plt.figure()
plt.plot(f, Sfjs)
plt.grid(True, 'both')
plt.xlabel('f')
plt.ylabel('S(f)')

# convert spectrum into wave elevation time series
N = len(f)
phase = np.random.uniform(0, 2*np.pi, N) #random phases
dw = omega[2]-omega[1] # d omega
amp = np.sqrt(2*Swjs*dw)

eta = np.zeros_like(ts)
for i in range(0, ts.size):
    eta[i] = np.sum(amp*np.cos((2*np.pi*f)*ts[i] + phase))
    
# plot wave elevation time series
plt.figure()
plt.plot(ts, eta)
plt.grid(True, 'both')
plt.xlabel('Time (s)')
plt.ylabel('$\eta$ (m)');

