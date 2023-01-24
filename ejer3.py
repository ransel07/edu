# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:32:01 2023

@author: rdrs_
"""

import matplotlib.pyplot as plt
import numpy
from scipy.stats import norm

x = numpy.linspace(1, 4, 4)
y = [.4,.3,.2,.1]

print (x)
print (y)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("probabilidad")
plt.title("Funcion De Probabilidad Normal")
plt.show()

