# EJECICIOS DE REGISTROS
persona = {
    'nombre': 'Juan',
    'edad': 35,
    'direccion': 'Calle Falsa 123'
}

libro = {
    'titulo': 'El señor de los anillos',
    'autor': 'J.R.R. Tolkien',
    'año': 1954,
    'genero': 'Fantasía'
}

pelicula = {
    'titulo': 'Star Wars',
    'director': 'George Lucas',
    'ano': 1977,
    'actores': ['Mark Hamill', 'Harrison Ford', 'Carrie Fisher']
}

# Crea un procedimiento llamado "imprimir_persona" que reciba como parámetro una variable de tipo "persona" y muestre en 
# pantalla los valores de sus campos. 

def imprimir_persona(persona):
    print(persona["nombre"])
    print(persona["edad"])
    print(persona["direccion"])

#imprimir_persona(persona)

# Crea un registro llamado "persona" que contenga los campos "nombre", "edad" y "dirección". Luego, crea una variable de 
# este tipo de registro y asígnale valores a sus campos.

persona["nombre"] = "Ransel"
persona["edad"] = 27
persona["direccion"] = "calle puerto rico #14"

# Crea una función llamada "edad_promedio" que reciba como parámetro un arreglo de variables de tipo "persona" y devuelva 
# como resultado la edad promedio de todas las personas en el arreglo.

persona1 = {
    "nombre" : "Rodrigo",
    "edad" : 33,
    "direccion" : "una calle hay numero algo"
}

persona2 = {
    "nombre" : "ana",
    "edad" : 28,
    "direccion" : "calle 13"
}

persona3 = {
    "nombre" : "Lorine",
    "edad" : 25,
    "direccion" : "zona colonial"
}

persona4 = {
    "nombre" : "Daneyris",
    "edad" : 30,
    "direccion" : "kings Landing"
}

personas = [persona["edad"], persona1["edad"], persona2["edad"], persona3["edad"], persona4["edad"]]
def edad_promedio(personas):
    sum = 0
    for edad in personas:
        sum = sum + edad
    promedio = sum / len(personas)
    print(promedio)

#edad_promedio(personas)

# Crea un registro llamado "libro" que contenga los campos "título", "autor" y "año_publicacion". Luego, crea una variable 
# de este tipo de registro y asígnale valores a sus campos.

libro["titulo"] = "Harry Potter y el Prisionero de Askaban"
libro["autor"] = "J.K. Rolling"
libro["año"] = 1999

# Crea un procedimiento llamado "imprimir_libro" que reciba como parámetro una variable de tipo "libro" y muestre en pantalla 
# los valores de sus campos.

def imprimir_libro(libro):
    print (libro)

#imprimir_libro(libro)

# Crea una función llamada "libros_por_autor" que reciba como parámetros un arreglo de variables de tipo "libro" y un nombre de 
# autor, y devuelva como resultado un arreglo con todos los libros escritos por ese autor.

libro1 = {
    'titulo': 'El señor de los anillos',
    'autor': 'J.R.R. Tolkien',
    'año': 1954,
    'genero': 'Fantasía'
}

libro2 = {
    'titulo': 'Game of Throne',
    'autor': 'George R. R. Martin',
    'año': 1996,
    'genero': 'Fantasía Medival'
}

libro3 = {
    'titulo': 'Los juegos del hambre',
    'autor': 'Suzanne Collins',
    'año': 2008,
    'genero': 'Ficción adulto joven'
}

libro4 = {
    'titulo': 'Danza de dragones',
    'autor': 'George R. R. Martin',
    'año': 2011,
    'genero': 'Fantasía Medival'
}

libros = []
libros_autores = [libro["autor"],libro1["autor"],libro2["autor"],libro3["autor"],libro4["autor"]]

def libros_por_autor(libros_autores):
    libros_george = []
    for lb in libros_autores:
        if lb == libro4["autor"]:
            libros_george.append(lb)
    print(libros_george)

libros_por_autor(libros_autores)

# Crea una función llamada "libros_por_año" que reciba como parámetros un arreglo de variables de tipo "libro" y un año, y devuelva 
# como resultado un arreglo con todos los libros publicados en ese año.

# Crea un registro llamado "estudiante" que contenga los campos "nombre", "edad", "promedio" y "becado". Luego, crea una variable de este tipo de registro y asígnale valores a sus campos.

# Crea una función llamada "mayores_edad" que reciba como parámetro un arreglo de variables de tipo "estudiante" y devuelva como resultado un arreglo con todos los estudiantes mayores de edad (edad >= 18).

# Crea una función llamada "promedio_mayor" que reciba como parámetro un arreglo de variables de tipo "estudiante" y devuelva como resultado un arreglo con todos los estudiantes que tienen un promedio mayor o igual a 4.0.

# Crea una función llamada "becados" que reciba como parámetro un arreglo de variables de tipo "estudiante" y devuelva como resultado un arreglo con todos los estudiantes que son becados (becado = true).
