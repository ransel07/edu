import regis_ejemp as re #
import struct            
import pickle


#_________________________________________________________________________________________________________
# Escribir una lista de números en un archivo binario y leerla luego

def f():
    lista = [1, 2, 3, 4, 5, 6, 10, 123, 850, 1030, 3540, 7550, 15000]
    with open("archivoDirecto.bin", "wb") as proof:
        for num in lista:
            proof.write(bytes(num)) # bytes() se utiliza para convertir en binario elemento como string, float o int
    with open("archivoDirecto.bin", "rb") as proof:
        lectura = proof.read()

#_________________________________________________________________________________________________________
# Copiar el contenido de un archivo de texto a otro:

def f():
    with open("archivoProof.txt", "w") as proof2:
        lista_base = re.empleados
        for reg in lista_base:
            proof2.write(str(reg) + "\n")
    with open("archivoProof.txt", "r") as proof2:
        lectura = proof2.readlines()
        with open("archivoProof2.txt", "w") as proof3:
            for r in lectura:
                proof3.write(str(r) + "\n")

#_________________________________________________________________________________________________________
# Crear un archivo de texto y contar el número de palabras:
def f():
    with open("ejemplosConteo.txt", "w") as x:
        lista = re.lista_productos
        for e in lista:
            x.write((str(e) + "\n"))
    with open("ejemplosConteo.txt", "r") as x:
        lectura2 = x.read()
        #print(len(lectura2))

#-----------------------------------------------------------------------------------------------------------------
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

#_________________________________________________________________________________________________________
#           Crea un archivo binario llamado "datos.bin" que contenga una 
#           lista de nombres y edades. Luego, escribe un programa que 
#           lea el archivo y muestre el nombre y la edad de cada persona.

def f():
    with open ("datos.bin", "wb") as dt:
        ls = re.personas
        for reg in ls:
            # Se le aplica la funsion encode() para convertirlos a binarios
            # se le aplica la el modulo struct con la funsion pack() para convertirlos en un pack
            #El formato 'is' indica que la cadena de bytes contiene un entero ('i') seguido de una 
            # cadena de caracteres ('s'). Si quisieras empacar más elementos, podrías utilizar un formato diferente.
            reg1 = reg["nombre"].encode()
            reg2 = reg["edad"]
            reg3 = reg["direccion"].encode()
            
            top = struct.pack('sis', reg1, reg2, reg3)
            #En este caso, no se utiliza la función pack() porque sólo se quiere escribir una 
            # cadena de bytes que contenga un salto de línea, y no empacar varios valores en una 
            # cadena de bytes.
            lineJump = "\n".encode()
            dt.write(top + lineJump) 
            
    with open("datos.bin", "rb") as dtr:
        # Se lee el contenido del archivo línea por línea
        for linea in dtr:
            try:
                nombre, edad, direccion = struct.unpack("sis", linea)
            except struct.error as e:
                print(f"Error al desempaquetar la línea: {e}")
                continue
            # Muestra el nombre y la edad de la persona.
            print(f"Nombre: {nombre} \n Edad: {edad} \n Dirección: {direccion}")



with open("date.bin", "wb") as archivo:
    persons = re.personas
    pickle.dump(persons, archivo)
with open("date.bin", "rb") as archivo:
    persons = pickle.load(archivo)
    for name, age, address in persons:
        print(f"Nombre: {name} \nEdad: {age} \nDirección: {address}")


