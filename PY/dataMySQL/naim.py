import mysql.connector

cnx = mysql.connector.connect(user="root", password="#0795Ran$el07#", host="localhost", database="for_education")

cursor = cnx.cursor()

query= "SELECT * FROM orders"
cursor.execute(query)
result = cursor.fetchall()

query= "SELECT * FROM persons"
cursor.execute(query)
result2 = cursor.fetchall()

for line in result:
    print (line)
for line2 in result2:
    print (line2)

cursor.close()
cnx.close()
