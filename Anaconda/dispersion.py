import numpy as np
import pandas as pd
import mysql.connector

u, p, h, d="root", "#0795Ran$el07#","localhost", "for_education"
cnx = mysql.connector.connect(user=u, password=p, host=h, database=d)
cursor = cnx.cursor()

query = "SELECT * FROM sex_toys"
datos = pd.read_sql_query(query, cnx)

rango = np.max(datos["price"]) - np.min(datos["price"])
varianza_poblacional = np.var(datos["price"])
varianza_muestral = np.var(datos["price"], ddof=1)
desv_est_pobl = np.std(datos["price"])
desv_est_muest = np.std(datos["price"], ddof=1)

print ("Rango: ", rango)
print ("Varianza Poblacional: ", varianza_poblacional)
print ("Varianza Muestral: ", varianza_poblacional)
print ("Desviación Estandar Poblacional: ", desv_est_pobl)
print ("Desviación Estandar Muestral: ", desv_est_muest)


cursor.close()
cnx.close()



