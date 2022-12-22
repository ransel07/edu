import regis_ejemp as re
import struct

# Escribir una lista de números en un archivo binario y leerla luego

lista = [1, 2, 3, 4, 5, 6, 10, 123, 850, 1030, 3540, 7550, 15000]
with open("archivoDirecto.bin", "wb") as proof:
    for num in lista:
        proof.write(bytes(num)) # bytes() se utiliza para convertir en binario elemento como string, float o int
with open("archivoDirecto.bin", "rb") as proof:
    lectura = proof.read()

# Copiar el contenido de un archivo de texto a otro:

with open("archivoProof.txt", "w") as proof2:
    lista_base = re.empleados
    for reg in lista_base:
        proof2.write(str(reg) + "\n")
with open("archivoProof.txt", "r") as proof2:
    lectura = proof2.readlines()
    with open("archivoProof2.txt", "w") as proof3:
        for r in lectura:
            proof3.write(str(r) + "\n")

# Crear un archivo de texto y contar el número de palabras:
with open("ejemplosConteo.txt", "w") as x:
    lista = re.lista_productos
    for e in lista:
        x.write((str(e) + "\n"))
with open("ejemplosConteo.txt", "r") as x:
    lectura2 = x.read()
    #print(len(lectura2))

# Leer un archivo de imágenes en formato JPEG y escribir un archivo 
# de imágenes en formato PNG
def f():
    with open("DALL·E 2022-10-16 20.59.32 - Cyberpunk.png", "rb") as picture:
        reads = picture.read()
    with open("DALL·E 2022-10-16 20.59.32 - Cyberpunk.jpeg", "wb") as picture:
        picture.write(reads)

    with open("Datos de la historia.docx", "rb") as picture: #Este codigo no es suficiente para la combersion porque al parece
        reads = picture.read()
    with open("Datos de la historia.pdf", "wb") as picture:
        picture.write(reads)

# Crea un archivo binario llamado "datos.bin" que contenga una 
# lista de nombres y edades. Luego, escribe un programa que 
# lea el archivo y muestre el nombre y la edad de cada persona.

with open ("datos.bin", "wb") as dt:
    ls = re.personas
    contador = 0
    for reg in ls:
        contador += 1
        # Se le aplica la funsion encode() para convertirlos a binarios
        # se le aplica la el modulo struct con la funsion pack() para convertirlos en un pack
        #El formato 'is' indica que la cadena de bytes contiene un entero ('i') seguido de una 
        # cadena de caracteres ('s'). Si quisieras empacar más elementos, podrías utilizar un formato diferente.
        top = struct.pack('is', contador, 'Registro #'.encode())
        #En este caso, no se utiliza la función pack() porque sólo se quiere escribir una 
        # cadena de bytes que contenga un salto de línea, y no empacar varios valores en una 
        # cadena de bytes.
        lineJump = "\n".encode()
        dt.write(top + lineJump) 
        for element in reg:
            #En el caso de las cadenas de caracteres, es necesario utilizar la función encode() 
            # para convertir las cadenas de caracteres en cadenas de bytes antes de empacarlas. 
            # Esto se debe a que la función pack() sólo puede empacar cadenas de bytes, no cadenas 
            # de caracteres.
            e = struct.pack('ss', element.encode(), " : ".encode()) 
            clave = str(reg[element]).encode() 
            dt.write(e + clave + lineJump)
with open("datos.bin", "rb") as dtr:
    # Se le aplica el metodo decode() para convertirlos a cadena de texto
    reading = dtr.read()
    (x, y) = struct.unpack("is", top) # (x, y) es porque a cada cual se le asigna lo elemento que se empaquetaron anteriormente
    print(x, y.decode()) # decode() para descodificar los bytes de la cadena de caracteres

    def f(): #colocado para deshabilitar 
        for reg in reading:
            struct.unpack(top)

            if element == (reg["nombre"]):
                    print(element)

# get() devuelve el valor de una clave específica en un diccionario.
