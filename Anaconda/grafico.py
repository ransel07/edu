# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 10:37:36 2023

@author: r.melenciano
"""

import pandas
import statistics

ruta = "sets\DR_real_estate_data_Nov_2020.csv"
datos = pandas.read_csv(ruta)
cabeza = datos.head(4)
price = datos["Price"]
forex = datos["Currency"]

count = 0
record = dict()
for num, fx in zip(price, forex):
    num = int(num.replace(",", ""))
    if 1000 < num:
        count =+ 1
        record[fx] = num

print (record)
print (count)


