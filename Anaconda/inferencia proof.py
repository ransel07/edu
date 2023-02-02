# import numpy as np
import pandas as pd
import scipy.stats as stats
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns

# GRAFICO DE DISPERSION

ruta = "C:/Users/rdrs_/OneDrive/Documentos/GitHub/Ste/Anaconda/sets/bienes_raices2020.csv"
dataf = pd.read_csv(ruta)
# print (dataf.head())

dataf["Price"] = dataf["Price"].str.replace(',','')
dataf["Area(m2)"] = dataf["Area(m2)"].str.replace(',','')
dataf["Price"] = dataf["Price"].fillna(1)
dataf["Area(m2)"] = dataf["Area(m2)"].fillna(1)


dataf["Price"] = dataf["Price"].astype(int)
dataf["Area(m2)"] = dataf["Area(m2)"].astype(int)

# print (dataf["Price"], dataf["Area(m2)"])
# for i, e in zip(dataf["Price"], dataf["Area(m2)"]):
    # print (type(i), type(e))
# print (type(dataf["Price"]), type(dataf["Area(m2)"]))




# plt.scatter(dataf["Price"], dataf["Area(m2)"])

# dataf1 = dataf[dataf[""] == 'I']
# sns.lmplot("x", "y", data = dataf1, fit_reg=True)


