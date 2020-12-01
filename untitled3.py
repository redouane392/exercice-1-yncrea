# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:44:47 2020

@author: Redouane
"""

 
import matplotlib.pyplot as plt
import random
x,y=(0.5,0.0)

abscisse = list()
ordonne = list()
for i in range(30000):   
    p= random.uniform(0,1)
    if p<=0.1: 

        xn=0.05*x
        yn=0.6*y
    if 0.1<p<=0.2:
        xn=0.05*x
        yn=-0.5*y+1.0
    if 0.2<p<=0.4:
        xn=0.46*x -0.32*y
        yn=0.39*x +0.38*y+0.6
    if 0.4<p<=0.6:
        xn=0.47*x -0.15*y
        yn=0.17*x +0.42*y+1.1
    if 0.6<p<0.8:
        xn=0.43*x+0.28*y
        yn= -0.25*x+0.45*y +1.0
    if p>=0.8:
        xn=0.42*x+0.26*y
        yn=-0.35*x+0.31*y+0.7
    x=xn
    y=yn
    abscisse.insert(0,xn)
    ordonne.insert(0,yn)
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
plt.plot(abscisse , ordonne,'r.')
plt.show()
