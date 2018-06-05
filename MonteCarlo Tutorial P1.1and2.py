#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 17:31:26 2018
MonteCarlo Tutorial P1.1and2
@author: jobelb
"""

import random
import matplotlib.pyplot as plt

x=[]
y=[]

#random.seed(555)
for i in range(0,10):
   x.append(random.random())

#random.seed(555)
for i in range(0,10):
   y.append(random.random())

plt.plot(x,y,'g*')
plt.xlabel('x')
plt.ylabel('y')
