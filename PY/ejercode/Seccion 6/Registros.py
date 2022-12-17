# EJECICIOS DE REGISTROS
import regis_ejemp

#imprimir_persona(persona)

# Crea un registro llamado "persona" que contenga los campos "nombre", "edad" y "dirección". Luego, crea una variable de 
# este tipo de registro y asígnale valores a sus campos.



# Crea una función llamada "edad_promedio" que reciba como parámetro un arreglo de variables de tipo "persona" y devuelva 
# como resultado la edad promedio de todas las personas en el arreglo.


def edad_promedio(personas):
    sum = 0
    for edad in personas:
        sum = sum + edad
    promedio = sum / len(personas)
    print(promedio)

#edad_promedio(personas)

# Crea un registro llamado "libro" que contenga los campos "título", "autor" y "año_publicacion". Luego, crea una variable 
# de este tipo de registro y asígnale valores a sus campos.



# Crea un procedimiento llamado "imprimir_libro" que reciba como parámetro una variable de tipo "libro" y muestre en pantalla 
# los valores de sus campos.

def imprimir_libro(libro):
    print (libro)

#imprimir_libro(libro)

# Crea una función llamada "libros_por_autor" que reciba como parámetros un arreglo de variables de tipo "libro" y un nombre de 
# autor, y devuelva como resultado un arreglo con todos los libros escritos por ese autor.

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



#print(estudiante)

# Crea una función llamada "mayores_edad" que reciba como parámetro un arreglo de variables de tipo "estudiante" 
# y devuelva como resultado un arreglo con todos los estudiantes mayores de edad (edad >= 18).



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





def carrito(productos):
    sum = 0
    for elemento in productos:
        sum = sum + elemento["precio"]
    print(sum)

#carrito(regis_ejemp.lista_productos)

# Crea una estructura de datos para representar un estudiante, con los siguientes campos: nombre (cadena de caracteres), 
# edad (entero), curso (cadena de caracteres) y calificación (flotante). Luego, cree una lista de estudiantes y utilice 
# un ciclo para calcular el promedio de calificación de todos los estudiantes en la lista.


def promedio_promedios(estudiantes):
    cant = len(estudiantes)
    sum = 0
    lista_promedios = []
    for est in estudiantes:
        contador = 0
        switch = True
        while switch:
            contador += 1
            if contador == est["promedio"]:
                lista_promedios.append(contador)
                switch = False
    for est2 in lista_promedios:                    # Luego de poner los promedios en una lista, se suman en este bucle
        sum =  sum + est2
    promedio = sum / cant
    print (lista_promedios)

#promedio_promedios(lista_estudiantes)

# Crea una estructura de datos para representar una persona, con los siguientes campos: nombre (cadena de caracteres), 
# edad (entero), dirección (cadena de caracteres), ciudad (cadena de caracteres) y pais (cadena de caracteres). 
# Luego, cree un diccionario de personas, donde la clave sea el nombre de la persona y el valor sea el registro de 
# la persona. Utiliza un ciclo para imprimir cada una de las personas en el diccionario.

registros = [    

    {"nombre": "Juan", "edad": 30, "dirección": "Calle Falsa 123", "ciudad": "Madrid", "pais": "España"}, 
    
    {"nombre": "Ana", "edad": 25, "dirección": "Calle Falsa 456", "ciudad": "Barcelona", "pais": "España"},

    {"nombre": "Pedro", "edad": 35, "dirección": "Calle Falsa 789", "ciudad": "Valencia", "pais": "España"},    
    
    {"nombre": "Sara", "edad": 28, "dirección": "Fake Street 123", "ciudad": "New York", "pais": "EE. UU."},
    ]

registro_rs = {"nombre": "Ransel", "edad": 28, "dirección": "Residencial Don Oscar", "ciudad": "SD de Guzman", "pais": "Rep. Dom."}

registros.append(registro_rs)


def imprimir(the_registro):
    person = {}
    for user in the_registro:
        person[user["nombre"]] = user
    #print(person)
    for user2 in person:
        print


# Crea una estructura de datos para representar un producto, con los siguientes campos: nombre (cadena de caracteres), 
# precio (flotante) y cantidad (entero). Luego, cree un diccionario de productos, donde la clave sea el nombre del 
# producto y el valor sea el registro del producto. Utiliza un ciclo para calcular el total de la compra de cada 
# producto en el diccionario.

# Crea una estructura de datos para representar una canción, con los siguientes campos: título (cadena de caracteres), 
# artista (cadena de caracteres) y duración (flotante en segundos). Luego, cree un diccionario de canciones, donde la 
# clave sea el título de la canción y el valor sea el registro de la canción. Utiliza un ciclo para calcular la 
# duración total de todas las canciones en el diccionario.

# Crea una estructura de datos para representar un estudiante, con los siguientes campos: nombre (cadena de caracteres), 
# edad (entero), curso (cadena de caracteres) y calificación (flotante). Luego, cree un diccionario de estudiantes, 
# donde la clave sea el nombre del estudiante y el valor sea el registro del estudiante. Utiliza un ciclo para calcular 
# el promedio de calificación de todos los estudiantes en el diccionario.