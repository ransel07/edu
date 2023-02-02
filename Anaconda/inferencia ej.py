# import numpy as np
import pandas as pd
import scipy.stats as stats
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns

# GRAFICO DE DISPERSION
dataf = sns.load_dataset("anscombe")

dataf1 = dataf[dataf["dataset"] == 'I']
sns.lmplot("x", "y", data = dataf1, fit_reg=True)

dataf2 = dataf[dataf["dataset"] == 'II']
sns.lmplot("x", "y", data = dataf2, fit_reg=True)

dataf3 = dataf[dataf["dataset"] == 'III']
sns.lmplot("x", "y", data = dataf3, fit_reg=True)

# CORRELACION

corr = 

# print (dataf["Price"], dataf["Area(m2)"])
# for i, e in zip(dataf["Price"], dataf["Area(m2)"]):
    # print (type(i), type(e))
# print (type(dataf["Price"]), type(dataf["Area(m2)"]))



