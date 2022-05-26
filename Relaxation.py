# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:21:11 2016

@author: ppxtmb
"""
import numpy as np
import matplotlib.pyplot as plt

tstart  = float(input('Choose Start Time!: '))
tstop   = float(input('Choose Stop Time!: '))

alpha   = float(input('Choose Your Field Dependence Power!: '))

beta    = float(input('Choose Your Temperature Dependence Power!: '))

t   = np.arange(tstart,tstop)
Bvalues = []
Tvalues = []

for n in range(0,4):
    n   = float(input('Choose Your Field Values!: '))
    Bvalues.append(n)
    
for m in range(0,4):
    m   = float(input('Choose Your Temperature Values!: '))
    Tvalues.append(m)
  
B_alpha = np.array(Bvalues)**alpha
T_beta  = np.array(Tvalues)**beta


a = 8.18
b   = 1384

M0a = (b*Bvalues[0])/Tvalues[0]
M0b = (b*Bvalues[1])/Tvalues[1]
M0c = (b*Bvalues[2])/Tvalues[2]
M0d = (b*Bvalues[3])/Tvalues[3]

T1a = (a*B_alpha[0])/T_beta[0]
T1b = (a*B_alpha[1])/T_beta[1]
T1c = (a*B_alpha[2])/T_beta[2]
T1d = (a*B_alpha[3])/T_beta[3]



Ma  = M0a*(1-np.exp(-t/T1a))
Mb  = M0b*(1-np.exp(-t/T1b))
Mc  = M0c*(1-np.exp(-t/T1c))
Md  = M0d*(1-np.exp(-t/T1d))

plt.figure(1)
plt.plot(t,Ma,'r')
plt.plot(t,Mb,'g')
plt.plot(t,Mc,'b')
plt.plot(t,Md,'c')

plt.xlabel('Time (mins)')
plt.ylabel('Signal')
plt.title('Simulation Showing Temp & Field Changes for Optimum Polarization')
plt.show()
 
b = np.array([np.nanmax(Ma),np.nanmax(Mb),np.nanmax(Mc),np.nanmax(Md)])
c = np.array([(1/Bvalues[0]),(1/Bvalues[1]),(1/Bvalues[2]),(1/Bvalues[3])])
        
plt.figure(2)    
plt.plot(c,b,'ro')
plt.show()    
 


    
