# Datos
# ==============================================================================
import pandas
import numpy
import matplotlib
from scipy import stats


ruta = "sets\DR_real_estate_data_Nov_2020.csv"
datos = pandas.read_csv(ruta)
top = datos.head(4)
price = datos["Price"]

list_price = []
for num in price:
    num = int(num.replace(",", ""))
    if 100 < num:
        list_price.append(num)
# datos = datos[(datos.age < 15) & (datos.male ==0)]
# weight = datos['weight']

# Histograma + curva normal teórica
# ==============================================================================

# Valores de la media (mu) y desviación típica (sigma) de los datos

mu, sigma = stats.norm.fit(list_price)

# Valores teoricos  de la normal en el rango observado

