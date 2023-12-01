import csv
import mysql.connector

# Crea una lista con los registros que quieres insertar
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    # Establece la conexión con la base de datos
    cnx = mysql.connector.connect(
        user='root', 
        password='#0795Ran$el07#', host='localhost', 
        database='Tablas_python', port="4848"
    )

    # Crea un cursor para realizar operaciones sobre la base de datos
    cursor = cnx.cursor()

    # Recorre cada fila del archivo CSV
    for fila in reader:
        # Crea una tupla con los datos de la fila
        datos = tuple(fila)
        # Ejecuta la consulta INSERT para insertar los datos en la tabla
        query = 'INSERT INTO Tabla (columna1, columna2, columna3) VALUES (%s, %s, %s)'
        cursor.execute(query, datos)
    
# Confirma los cambios
cnx.commit()

# Cierra el cursor y la conexión con la base de datos
cursor.close()
cnx.close()