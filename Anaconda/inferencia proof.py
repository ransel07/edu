import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as stats
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# GRAFICO DE DISPERSION

ruta = "C:/Users/rdrs_/OneDrive/Documentos/GitHub/Ste/Anaconda/csv_inmobiliario.csv"
dataf = pd.read_csv(ruta)
price = dataf["Price"].to_numpy()
area = dataf["Area(m2)"].to_numpy()
price = price.reshape(-1, 1)
area = area.reshape(-1, 1)
# print (dataf.head())

# REGRESION LINEAL SIMPLE
print (price)
print (area)
reg = LinearRegression().fit(price, area)

# y_pred = reg.predict(price)

print (reg)


































