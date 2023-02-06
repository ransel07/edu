import mysql.connector
import pandas as pd


u, p, h, d="root", "#0795Ran$el07#","localhost", "for_education"
cnx = mysql.connector.connect(
    user=u, 
    password=p, 
    host=h, 
    database=d
    )

path = "C:\Users\rdrs_\OneDrive\Documentos\GitHub\Ste\Anaconda\sets\bienes_raices2020.csv"
read = pd.read_csv(path, interator=True, chunksize=1)

cursor = cnx.cursor()

query = "SELECT * FROM sex_toys"

dat = pd.read_sql_query(query, cnx)

cursor.close()
cnx.close()