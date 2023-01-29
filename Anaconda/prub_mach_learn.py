# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

url = 'https://raw.githubusercontent.com/JoaquinAmatRodrigo/Estadistica-machine-learning-python/master/data/Howell1.csv'
read = pd.read_csv(url, sep=",")

print(read.head(6))
#print ("Cantidad de Filas y columnas: ", read.shape)
#print ("Nombre columnas: ", read.columns)
#print (read.info())
#print (read.describe())

# CORRELACION

# corr = read.set_index("age").corr()
# sm.graphics.plot_corr(corr, xnames=list(corr.columns))
# plt.show()

pop = read[read["height"] > 150]
print (pop.head(6))

pop1 = read[read["weight"] > 50]
pop.drop(['height'],axis=1)['age'].plot(kind='bar')




























