# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:57:36 2023

@author: gebo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def planimetersolve(x, y,dx,dy,tspan, theta0, l, N=50):
    #   planimetersolve(x, y,dx,dy,tspan, theta0, l):
    #   computes the motion of a Prytz planimeter:
    #   INPUT:
    #   x,y: functions returning x and y position of tracer end.
    #   dx,dy: derivatives of x,y
    #   theta0: initial angle of planimeter arm
    #   tsoan=[t0, tend]: parametrization interval
    #   l: length of planimeter arm
    #   OUTPUT: X,Y,XX,YY, TH
    #   X,Y: positions of tracer end
    #   XX,YY: positions of chisel end
    #   TH:    angles
     
    def f(t,y):
        return 1/l*(np.sin(y)*dx(t)-np.cos(y)*dy(t))
    sol = solve_ivp(f, tspan, [theta0],t_eval=np.linspace(tspan[0], tspan[1], N), method='DOP853', atol=1e-12, rtol=1e-12)
    T=sol.t.flatten()
    TH=sol.y.flatten()
    

    X=x(T)
    Y=y(T)

    
    return X,Y,TH

def planimeterplot(X,Y,TH,l):
    
    XX=X+l*np.cos(TH)
    YY=Y+l*np.sin(TH)
    
    xarc = X[0]+l*np.cos(np.linspace(TH[0],TH[-1]))
    yarc = Y[0]+l*np.sin(np.linspace(TH[0],TH[-1]))
    
    fig, ax =plt.subplots()
    
    ax.plot(X,Y, XX,YY)
    ax.plot(X[0],Y[0], '.')
    ax.plot(xarc,yarc, '--')
    ax.set_aspect('equal')
    
    AP=l**2*(TH[-1]-TH[0])
    ax.set_title('A ≈ '+ str(round(AP,3)))
    
    return fig, ax