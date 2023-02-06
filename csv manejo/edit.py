import numpy as np
import pandas as pd
import scipy.stats as stats
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns

# GRAFICO DE DISPERSION
ruta = "C:/Users/rdrs_/OneDrive/Documentos/GitHub/Ste/Anaconda/sets/bienes_raices2020.csv"
dataf = pd.read_csv(ruta)
print (dataf.head())
# print (dataf.info())

print (dataf["Area(m2)"])

# ELIMINAR COMAS
dataf["Price"] = dataf["Price"].str.replace(',','')
dataf["Area(m2)"] = dataf["Area(m2)"].str.replace(',','')

# RELLENAR VALORES NaN
dataf["Price"] = dataf["Price"].fillna(1)
dataf["Area(m2)"] = dataf["Area(m2)"].fillna(1)

# CONVERTIR EN "INT"
dataf["Price"] = dataf["Price"].astype(int)
dataf["Area(m2)"] = dataf["Area(m2)"].astype(int)

# CAMBIAR 1 POR NaN
# dataf.loc[dataf["Price"].eq(1), "Price"] = np.NaN
# dataf.loc[dataf["Area(m2)"].eq(1), "Area(m2)"] = np.NaN
# dataf["Price"] = dataf["Price"].replace(1, np.NaN, inplace=True)
# dataf["Area(m2)"] = dataf["Area(m2)"].replace(1, np.NaN, inplace=True)

# CAMBIAR "X", CUANDO "X" ESTA EN UN RANGO EN ESPECIFICO, POR NaN
dataf.loc[(dataf["Price"] >= 1) & (dataf["Price"] <= 500), "Price"] = np.NaN
dataf.loc[(dataf["Area(m2)"] >= 1) & (dataf["Area(m2)"] <= 10), "Area(m2)"] = np.NaN

# COLOCAR DONDE ESTE NaN ELEMENTO INTERPOLADOS
dataf["Price"].interpolate(method="linear", inplace=True)
dataf["Area(m2)"].interpolate(method="linear", inplace=True)

# COLOCAR DONDE ESTE NaN ELEMENTO INTERPOLADOS, todo basandoce en datos de otre columna
# dataf["Area(m2)"] = dataf["Area(m2)"].interpolate(
#     method="spline", 
#     values=dataf["Rooms"]
#     )

dataf.to_csv("csv_inmobiliario.csv", index= False)





