import numpy as np
import pandas as pd
import scipy.stats as stats
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns

# GRAFICO DE DISPERSION
dataf = sns.load_dataset("anscombe")

dataf1 = dataf[dataf["dataset"] == 'I']
# sns.lmplot("x", "y", data = dataf1, fit_reg=True)

dataf2 = dataf[dataf["dataset"] == 'II']
# sns.lmplot("x", "y", data = dataf2, fit_reg=True)

dataf3 = dataf[dataf["dataset"] == 'III']
# sns.lmplot("x", "y", data = dataf3, fit_reg=True)

# CORRELACION

datos = np.random.rand(5, 4)

np.corrcoef(datos[0], datos[1])

# COVARIANZA 

def Cov (xs, ys, meanx=None, meany=None):
    xs = np.asarray(xs)
    ys = np.asarray(ys)
    
    if meanx is None:
        meanx = np.mean(xs)
    if meany is None:
        meany = np.mean(ys)

    cov = np.dot(xs-meanx, ys-meany) / len(xs)
    return cov

cov = Cov(dataf["x"], dataf["y"])

cov2 = np.cov(dataf["x"], dataf["y"]) 

# CORRELACION DE PEARSON (Si las variable son lineales)

s = stats.pearsonr(dataf3["x"], dataf3["y"])
# sns.lmplot("x", "y", data = dataf1, fit_reg=False)

# sns.jointplot(dataf1["x"], dataf1["y"])

# TEST DE HIPOTESIS

datos_random1 = np.random.normal (0, 1, size=50)
datos_random2 = np.random.normal (2, 1, size=50)

plt.hist(datos_random1)
plt.hist(datos_random2)


















