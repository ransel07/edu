import pandas as pd
import numpy as np
import mysql.connector

u, p, h, d="root", "#0795Ran$el07#","localhost", "for_education"
cnx = mysql.connector.connect(user=u, password=p, host=h, database=d)
cursor = cnx.cursor()

query = "SELECT * FROM sex_toys"

# "MUESTREO ALEATORIO SIMPLE"
datos = pd.read_sql_query(query, cnx)

# "MUESTREO RENGLONES"
renglones = datos.sample(frac = 0.10)

# "MUESTREO DE ELEMENTO DE UNA COLUMNA"
muestra_peso = np.random.choice(datos["height"], 10)

print (datos)
print (renglones)
print (muestra_peso)

cursor.close()
cnx.close()


