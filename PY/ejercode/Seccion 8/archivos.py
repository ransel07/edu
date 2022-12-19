# Crea un archivo de texto llamado "ejercicio1.txt" y escribe algunas líneas de 
# texto en él. Luego, abre el archivo en modo de lectura y muestra su contenido 
# en pantalla.

def archivo():
    nuevo_arch = open("ejercicio1.txt", "r")
    #nuevo_arch.write("Bienvenido al mundo real")
    #nuevo_arch_read = open("ejercicio1.txt", "r")
    r = nuevo_arch.read()
    print(r)
    nuevo_arch.close()

#archivo()

# Crea un archivo de texto llamado "ejercicio2.txt" y escribe algunas líneas de 
# texto en él. Luego, abre el archivo en modo de escritura y sobrescríbelo con 
# un nuevo conjunto de líneas de texto.

#with open("ejercicio2.txt", "w") as ej2:
    #abrir = open("ejercicio1.txt", "w")
    #w = ej2.write("Nueva linea de texto")

# Crea un archivo de texto llamado "ejercicio3.txt" y escribe algunas líneas de 
# texto en él. Luego, abre el archivo en modo de adición y agrega una nueva 
# línea al final del archivo.

linea = ["No volver a manocear a la maestra", "porque esta mal\n"]

def funsion():
    with open("ejercicio3.txt", "w") as ej3:
        ej3.writelines(linea)

    with open("ejercicio3.txt", "a") as ejer3:
        ejer3.write("Adios idiotas\n")

# Crea un archivo de texto llamado "ejercicio4.txt" y escribe algunas líneas de 
# texto en él. Luego, abre el archivo en modo de lectura y cuenta cuántas 
# líneas hay en el archivo utilizando un bucle for.

lines = ["1ra linea\n", "2da linea\n", "3ra linea\n", "4ta linea\n", "5ta linea\n"]

def funsion():
    with open("ejercicio4.txt", "w") as ej4:
        ej4.writelines(lines)

    with open("ejercicio4.txt", "r") as ej04:
        contador = 0
        for i in lines:
            contador += 1
        print(f"{contador} es el numero de lineas que tiene ejercicio4.txt")

# Crea un archivo de texto llamado "ejercicio5.txt" y escribe algunas líneas 
# de texto en él. Luego, abre el archivo en modo de lectura y busca una 
# palabra específica en el archivo utilizando un bucle for. Si encuentras 
# la palabra, muestra un mensaje en pantalla indicando en qué línea se 
# encontró.

#with open("ejercicio5.txt", "w") as e5:
    #e5.writelines(lines)

def funsion():
    with open("ejercicio5.txt", "r") as e5:
        conteo = 0
        for elemento in e5:
            conteo = conteo + 1
            encuentra = elemento.find("linea")
            if encuentra > 0:
                #print(f"se encuentra en la posicion {encuentra} de la linea {conteo}")
                break

#def suma_palabras():
    p = ["Esta texo en un ", "ejemplo ", "para resolver ", "un ejercicio"]
    i = []
    l = ""
    for element in p:
        l = l + element
    #print(l)        

# Crea un archivo de texto con información sobre diferentes libros (título, 
# autor, año de publicación, etc.). Luego, escribe un programa en Python que 
# lea el archivo y muestre toda la información de cada libro en un formato 
# legible para el usuario.

import regis_ejemp as re

def funsion():
    with open("ejercicio6.txt", "w") as e6:
        for elemento in re.libros_titulo1:
            e6.write(str(elemento) + "\n")

    with open("ejercicio6.txt", "r") as e6:
        lineas = e6.readlines()
        for linea in lineas:
            print(linea)

# Crea un archivo de texto que contenga información sobre diferentes empleados 
# de una empresa (nombre, cargo, salario, etc.). Luego, escribe un programa en 
# Python que lea el archivo y muestre el salario total de todos los empleados.

def funsion():
    with open("ejercicio7.txt", "w") as arch:
        for elemento in re.empleados:
            arch.write(str(elemento) + "\n")

    with open("ejercicio7.txt", "r") as arch:
        lineas = arch.readlines()
        for elemento in arch:
            print(elemento)


# Crea un archivo de texto que contenga información sobre diferentes productos 
# en una tienda (nombre, precio, cantidad disponible, etc.). Luego, escribe un 
# programa en Python que lea el archivo y permita al usuario comprar un producto 
# específico, actualizando la cantidad disponible en el archivo después de la 
# compra.


def fun():
    with open("productos.txt", "w") as productos:
        contar = 0
        for elemento in re.lista_productos:
            contar = contar + 1
            visual = "---------------- " + elemento["nombre"] + " ----------------\n"
            productos.writelines(" \n" + visual)
            for sub in elemento.keys():
                productos.writelines(str(sub) + " : " + str(elemento[sub]) + "\n")
    with open ("productos.txt", "r") as productos:
        lineas = productos
        for linea in lineas:
            print(linea)
#fun()
def buyProduct():
    buy = input()
    cant_buy = input()
    if buy == 0:
        p = {re.producto["cantidad disponible"] - cant_buy}
        print (p)

#buyProduct()

# Crea un archivo de texto que contenga información sobre diferentes estudiantes 
# y sus calificaciones en un curso (nombre, notas en cada examen, promedio final, 
# etc.). Luego, escribe un programa en Python que lea el archivo y muestre la 
# lista de estudiantes ordenada por promedio final.



# Crea un archivo de texto con información sobre diferentes estudiantes y sus 
# calificaciones en un curso (nombre, notas en cada examen, promedio final, etc.). 
# Luego, escribe un programa en Python que lea el archivo y almacene la información 
# de cada estudiante en un registro. Utiliza un arreglo de estos registros para 
# luego mostrar la lista de estudiantes ordenada por promedio final.

# Crea un archivo de texto con información sobre diferentes productos en una tienda 
# (nombre, precio, cantidad disponible, etc.). Luego, escribe un programa en Python 
# que lea el archivo y almacene la información de cada producto en un registro. 
# Utiliza un arreglo de estos registros para luego permitir al usuario buscar un 
# producto específico por nombre y mostrar toda su información.

# Crea un archivo de texto con información sobre diferentes empleados de una empresa 
# (nombre, cargo, salario, etc.). Luego, escribe un programa en Python que lea el archivo 
# y almacene la información de cada empleado en un registro. Utiliza un arreglo de estos 
# registros para luego calcular el salario total de todos los empleados y mostrar el 
# promedio de salarios por cargo.

# Crea un archivo de texto con información sobre diferentes libros (título, autor, año de 
# publicación, etc.). Luego, escribe un programa en Python que lea el archivo y almacene 
# la información de cada libro en un registro. Utiliza un arreglo de estos registros para 
# luego permitir al usuario buscar libros por año de publicación y mostrar todos los 
# títulos y autores de los libros publicados en ese año.
