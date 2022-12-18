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

with open("ejercicio3.txt", "w") as ej3:
    ej3.writelines(linea)

with open("ejercicio3.txt", "a") as ejer3:
    ejer3.write("Adios idiotas\n")

# Crea un archivo de texto llamado "ejercicio4.txt" y escribe algunas líneas de 
# texto en él. Luego, abre el archivo en modo de lectura y cuenta cuántas 
# líneas hay en el archivo utilizando un bucle for.

lines = ["1ra linea\n", "2da linea\n", "3ra linea\n", "4ta linea\n", "5ta linea\n"]

with open("ejercicio4.txt", "w") as ej4:
    ej4.writelines(lines)

with open("ejercicio4.txt", "r") as ej04:
    contador = 0
    for i in lines:
        contador += 1
    #print(f"{contador} es el numero de lineas que tiene ejercicio4.txt")

# Crea un archivo de texto llamado "ejercicio5.txt" y escribe algunas líneas de 
# texto en él. Luego, abre el archivo en modo de lectura y busca una palabra 
# específica en el archivo utilizando un bucle for. Si encuentras la palabra, 
# muestra un mensaje en pantalla indicando en qué línea se encontró.

with open("ejercicio5.txt", "w") as e5:
    e5.writelines(lines)

with open("ejercicio5.txt", "r") as e5:
    for palabra in e5:
        print(palabra)
        if palabra == "1ra linea":
            e5.find("linea")
            repite = e5.count(palabra)
            print("la palabra {palabra}, se encuentra {repite}")

