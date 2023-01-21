import mysql.connector

cnx = mysql.connector.connect(user='root', password='#0795Ran$el07#', host='localhost', port="4848")

cursor = cnx.cursor()

query2 = 'USE Tablas_python;'
cursor.execute(query2)
query3 = 'CREATE TABLE '
cursor.execute(query3)

cnx.commit()

cursor.close()
cnx.close()