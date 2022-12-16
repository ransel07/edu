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

libros_autores = [libro["autor"],libro1["autor"],libro2["autor"],libro3["autor"],libro4["autor"]]
libros_titulo = [libro["titulo"],libro1["titulo"],libro2["titulo"],libro3["titulo"],libro4["titulo"]]
libros_titulo1 = [libro, libro1, libro2, libro3, libro4]
lbn = [libro]
autor = libro['autor']

def libros_por_autor(libros, nombre_autor):
    libros_del_autor = []
    for lib in libros:
        if lib["autor"] == nombre_autor:
            libros_del_autor.append(lib["titulo"])
    print (libros_del_autor)

#libros_por_autor(libros_titulo1, libro2["autor"])

# Crea una función llamada "libros_por_año" que reciba como parámetros un arreglo de variables de tipo "libro" y 
# un año, y devuelva como resultado un arreglo con todos los libros publicados en ese año.

def libros_por_año(libros, año):
    titulo_lib = []
    for lib in libros:
        if lib["año"] == año:
            titulo_lib.append(lib["titulo"])
    cant = len(titulo_lib)
    if cant > 0:
        print("Este es/son el/los libro/s de dicho año ", titulo_lib)
    else:
        print("no se encuentra ningun libro de este año")

#libros_por_año(libros_titulo1, libro2["año"])

# Crea un registro llamado "estudiante" que contenga los campos "nombre", "edad", "promedio" y "becado". Luego, 
# crea una variable de este tipo de registro y asígnale valores a sus campos.

estudiante = {
    "nombre" : "",
    "edad" : "",
    "promedio" : "",
    "becado" : ""
}

estudiante1 = {
    "nombre" : "Rodrigo",
    "edad" : 33,
    "promedio" : 2.9,
    "becado" : "si"
}

estudiante2 = {
    "nombre" : "ana",
    "edad" : 17,
    "promedio" : 4.0,
    "becado" : "si"
}

estudiante3 = {
    "nombre" : "Lorine",
    "edad" : 25,
    "promedio" : 2.0,
    "becado" : "no"
}

estudiante4 = {
    "nombre" : "Daneyris",
    "edad" : 30,
    "promedio" : 3.0,
    "becado" : "si"
}

estudiante["nombre"] = "David" 
estudiante["edad"] = 30 
estudiante["promedio"] = 4.0 
estudiante["becado"] = "si"

#print(estudiante)

# Crea una función llamada "mayores_edad" que reciba como parámetro un arreglo de variables de tipo "estudiante" 
# y devuelva como resultado un arreglo con todos los estudiantes mayores de edad (edad >= 18).

lista_estudiantes = [estudiante,estudiante1,estudiante2,estudiante3,estudiante4]

def mayores_edad(variabble_estudiante):
    adultos = []
    menores = []
    for est in variabble_estudiante:
        if est["edad"] >= 18:
            adultos.append(est["nombre"])
        else:
            menores.append(est["nombre"])
    print("LOS MAYORES DE EDAD SON: ")
    for mayor in adultos:
        print(mayor)
    print("LOS MENORES SON: ")
    for menor in menores:
        print(menor)

#mayores_edad(lista_estudiantes)

# Crea una función llamada "promedio_mayor" que reciba como parámetro un arreglo de variables de tipo "estudiante" 
# y devuelva como resultado un arreglo con todos los estudiantes que tienen un promedio mayor o igual a 4.0.

def promedio_mayor(variabble_estudiante):
    resultado = []
    for est in variabble_estudiante:
        if est["promedio"] >= 4.0:
            resultado.append(est["nombre"])
    print(resultado)

#promedio_mayor(lista_estudiantes)

# Crea una función llamada "becados" que reciba como parámetro un arreglo de variables de tipo "estudiante" y 
# devuelva como resultado un arreglo con todos los estudiantes que son becados (becado = true).

def becados(variabble_estudiante):
    est_becados = []
    for est in variabble_estudiante:
        if est["becado"] == "si":
            est_becados.append(est["nombre"])
    print(est_becados)

#becados(lista_estudiantes)

#Crea una estructura de datos para representar un producto, con los siguientes campos: nombre (cadena de caracteres), 
# precio (flotante) y cantidad (entero). Luego, cree una lista de productos y utilice un ciclo para calcular el total 
# de la compra de cada producto en la lista.

producto = {
    "nombre" : "Ram",
    "precio" : 75.5,
    "cantidad" : 1,
}

producto1 = {
    "nombre" : "Board",
    "precio" : 200.0,
    "cantidad" : 1,
}

producto2 = {
    "nombre" : "Tarjeta de Video",
    "precio" : 298.3,
    "cantidad" : 1,
}

producto3 = {
    "nombre" : "SSD m.2",
    "precio" : 93.8,
    "cantidad" : 1,
}

lista_productos = [producto, producto1, producto2, producto3]

def carrito(productos):
    sum = 0
    for elemento in productos:
        sum = sum + elemento["precio"]
    print(sum)

carrito(lista_productos)

#Crea una estructura de datos para representar una canción, con los siguientes campos: título (cadena de caracteres), 
# artista (cadena de caracteres) y duración (flotante en segundos). Luego, cree una lista de canciones y utilice un 
# ciclo para calcular la duración total de todas las canciones en la lista.



#Crea una estructura de datos para representar un estudiante, con los siguientes campos: nombre (cadena de caracteres), 
# edad (entero), curso (cadena de caracteres) y calificación (flotante). Luego, cree una lista de estudiantes y utilice 
# un ciclo para calcular el promedio de calificación de todos los estudiantes en la lista.

def promedio_promedios(estudiantes):
    for est in estudiantes:
        estudiantes.count(est[""])

#Crea una estructura de datos para representar una persona, con los siguientes campos: nombre (cadena de caracteres), 
# edad (entero), dirección (cadena de caracteres), ciudad (cadena de caracteres) y estado (cadena de caracteres). 
# Luego, cree un diccionario de personas, donde la clave sea el nombre de la persona y el valor sea el registro de 
# la persona. Utiliza un ciclo para imprimir cada una de las personas en el diccionario.

#Crea una estructura de datos para representar un producto, con los siguientes campos: nombre (cadena de caracteres), 
# precio (flotante) y cantidad (entero). Luego, cree un diccionario de productos, donde la clave sea el nombre del 
# producto y el valor sea el registro del producto. Utiliza un ciclo para calcular el total de la compra de cada 
# producto en el diccionario.

#Crea una estructura de datos para representar una canción, con los siguientes campos: título (cadena de caracteres), 
# artista (cadena de caracteres) y duración (flotante en segundos). Luego, cree un diccionario de canciones, donde la 
# clave sea el título de la canción y el valor sea el registro de la canción. Utiliza un ciclo para calcular la 
# duración total de todas las canciones en el diccionario.

#Crea una estructura de datos para representar un estudiante, con los siguientes campos: nombre (cadena de caracteres), 
# edad (entero), curso (cadena de caracteres) y calificación (flotante). Luego, cree un diccionario de estudiantes, 
# donde la clave sea el nombre del estudiante y el valor sea el registro del estudiante. Utiliza un ciclo para calcular 
# el promedio de calificación de todos los estudiantes en el diccionario.