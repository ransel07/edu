import mysql.connector
import pandas as pd


u, p, h, d="root", "#0795Ran$el07#","localhost", "for_education"
cnx = mysql.connector.connect(
    user=u, 
    password=p, 
    host=h, 
    database=d
    )

cursor = cnx.cursor()

query = "SELECT * FROM productos"

df = pd.read_sql_query(query, cnx)

print (df.head(4))
print (df.info())










