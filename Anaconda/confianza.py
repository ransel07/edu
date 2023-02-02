import numpy as np
import pandas as pd
import scipy.stats as stats
from math import sqrt

ruta = "\Anaconda\sets\bienes_raices2020.csv"
dato = pd.read_csv(ruta)
precio = dato["Price"]

# INTERVALO DE CONFIANZA

c = stats.norm.interval(alpha = 0.95,
                        loc = np.mean(precio),
                        scale = precio.std(ddof=1)/sqrt(precio.size))
c2 = (precio.mean() - 1.960*(precio.std(ddof=1)/sqrt(precio.size)),
      precio.mean() + 1.960*(precio.std(ddof=1)/sqrt(precio.size)))


print("\nCálculo de valores z para un cierto Nivel de Confianza\n")
print ("90%:", stats.norm.ppf(1 - (1 - 0.90)/2))
print ("95%:", stats.norm.ppf(1 - (1 - 0.95)/2))
print ("99%:", stats.norm.ppf(1 - (1 - 0.99)/2))


