import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import math

def Personal_Plot(x, y):
    plt.plot(x,y)

    plt.xlabel("")
    plt.ylabel("")
    plt.title("")

    # MOSTRAS EJE CARTECIANO
    plt.axhline(0, color="black", lw=2)
    plt.axvline(0, color="black", lw=2)
    plt.show()

class InfoPlot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot_(self):
        plt.plot(self.x, self.y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Si, aja")
        plt.axhline(0, color="black", lw=2)
        plt.axvline(0, color="black", lw=2)
        return plt.show()

x = np.linspace(-10, 10, num=100)
y = (x**2) - x + 2

Personal_Plot(x, y)


