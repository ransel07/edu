# Datos
# ==============================================================================
import pandas
import numpy
import matplotlib


ruta = "sets\DR_real_estate_data_Nov_2020.csv"
datos = pandas.read_csv(ruta)
print(datos.info())
# print (datos.head(4))
datos.head(4)
price = datos["Price"]
for num in price:
    num = num.replace(",", "")
    if int(num) < 1000:
        print (datos["Municipality"])
# datos = datos[(datos.age < 15) & (datos.male ==0)]
# weight = datos['weight']


