# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
import statistics

ruta = "sets\DR_real_estate_data_Nov_2020.csv"
datos = pandas.read_csv(ruta)
price = datos["Price"]

lista = []
for num in price:
    num = int(num.replace(",", ""))
    if 1000 < num:
        lista.append(num)

# ------ MEDIDA DE TENDENSIA CENTRAL --------
media_aritmetica = statistics.mean(lista)
mediana = statistics.median(lista)
moda = statistics.mode(lista)
repeticiones = lista.count(moda)

print (lista)
print ("")
print (media_aritmetica, mediana, moda, "Se repite", repeticiones, "veces")

# --------- MEDIDA DE DISPERSION
rango = max(lista) - min(lista)
desviacion_estandar = statistics.stdev(lista)
varianza = statistics.variance(lista)
print ("")
print (rango, desviacion_estandar, varianza)





