# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# pylab inline
from scipy.integrate import odeint



#population
N = 10000000

# initial Conditions
I0 = 400000
R0 = 35000
S0 = N - I0 - R0


#infection rate

beta = 0.2

#recovery rate per day

gamma = R0/I0


def model(z,t):
    s = z[0]
    i = z[1]
    r = z[2]
    
    dsdt = -beta * i * s / N 
    didt = beta * i * s / N  - gamma*i
    drdt = gamma * i
    
    return [dsdt,didt,drdt]

ts = np.linspace(0,50,50)
z0 = [S0,I0,R0]
zs = odeint(model,z0,ts)

s = zs[:,0]
i = zs[:,1]
r = zs[:,2]

plt.plot(ts,s,label ='suceptible')
plt.plot(ts,i,label = 'infected')
plt.plot(ts,r,label = 'recovered')
plt.legend()
plt.xlabel('time')
plt.ylabel('Population');