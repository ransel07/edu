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


def f():
    with open("date.bin", "wb") as archivo:
        persons = re.personas
        pickle.dump(persons, archivo)
    with open("date.bin", "rb") as archivo:
        persons = pickle.load(archivo)
        for name, age, address in persons:
            print(f"Nombre: {name} \nEdad: {age} \nDirección: {address}")

#_________________________________________________________________________________________________________
# Crea un archivo binario llamado "datos_alumnos.bin" que contenga una lista de nombres, 
# edades y calificaciones de cada alumno. Luego, escribe un programa que lea el archivo y 
# muestre el nombre, edad y calificación de cada alumno.
def f():
    with open("datos_alumnos.bin", "wb") as dtalumn:
        estudiantes = re.estudiantes
        pickle.dump(estudiantes, dtalumn)
    with open("datos_alumnos.bin", "rb") as dtalumn:
        alumnos = pickle.load(dtalumn)
        for reg in alumnos:
            for elemento in reg:
                name = reg["nombre"]
                age = reg["edad"]
                promedio = reg["promedio"]
            print(f"Nombre: {name}\nEdad: {age}\nPromedio: {promedio}")


#_________________________________________________________________________________________________________
# Crea un archivo binario llamado "datos_empleados.bin" que contenga una lista de nombres, 
# edades, puestos de trabajo y salarios de cada empleado. Luego, escribe un programa que 
# lea el archivo y muestre el nombre, edad, puesto de trabajo y salario de cada empleado.

def f():
    with open("datos_empleados.bin", "wb") as P_staff:
        employees = re.empleados
        write = pickle.dump(employees, P_staff)
    with open("datos_empleados.bin", "rb") as P_staff:
        readStaff = pickle.load(P_staff)
        contador = 0
        for group in readStaff:
            contador += 1
            top = " "
            name = group["nombre"]
            age = group["edad"]
            print(f"----Empleado {contador}-----\n\nNombre: {name}\nEdad: {age}\n")

#_________________________________________________________________________________________________________

# Crea un archivo binario llamado "datos_clientes.bin" que contenga una lista de nombres, 
# edades, direcciones y números de teléfono de cada cliente. Luego, escribe un programa que 
# lea el archivo y muestre el nombre, edad, dirección y número de teléfono de cada cliente.

# Crea un archivo binario llamado "datos_productos.bin" que contenga una lista de nombres, 
# precios y descripciones de cada producto. Luego, escribe un programa que lea el archivo 
# y muestre el nombre, precio y descripción de cada producto.


# Crea un archivo binario llamado "datos_mascotas.bin" que contenga una lista de nombres, 
# edades y tipos de mascotas de cada dueño. Luego, escribe un programa que lea el archivo y 
# muestre el nombre, edad y tipo de mascota de cada dueño.

#_________________________________________________________________________________________________________
# Crea un programa que lea un archivo binario que contenga información sobre una lista de 
# productos (nombre, precio, cantidad en stock). Luego, escribe una función que calcule el 
# valor total en stock de cada producto y muestre el resultado.

def f():
    with open("productos.bin", "wb") as datoBin:
        catalog = re.lista_productos
        write = pickle.dump(catalog, datoBin)
    with open("productos.bin", "rb") as datoBin:
        read = pickle.load(datoBin)
        for article in read:
            name = article["nombre"]
            cant = article["cantidad disponible"]
            vaule = article["precio"]
            total = cant * vaule
            print(f"Valor total de los {name} es de USD${total}")


# Crea un programa que lea un archivo binario que contenga información sobre una lista de 
# clientes (nombre, dirección, número de teléfono). Luego, escribe una función que permita 
# buscar un cliente por nombre y muestre su información completa.

# Crea un programa que lea un archivo binario que contenga información sobre una lista de 
# empleados (nombre, cargo, salario). Luego, escribe una función que permita calcular el 
# salario total de la empresa y muestre el resultado.

# Crea un programa que lea un archivo binario que contenga información sobre una lista de 
# libros (título, autor, año de publicación). Luego, escribe una función que permita buscar 
# libros por autor y muestre todos los títulos escritos por ese autor.

# Crea un programa que lea un archivo binario que contenga información sobre una lista de 
# películas (título, director, año de estreno). Luego, escribe una función que permita buscar 
# películas por año de estreno y muestre todos los títulos estrenados en ese año.





# Crea un archivo binario llamado "empleados.bin" que contenga una lista de empleados de 
# una empresa. Cada empleado debe tener un número de identificación único, nombre, edad, 
# género y puesto de trabajo. Escriba un programa que lea el archivo y muestre toda la 
# información de cada empleado.

with open("empleados.bin", "wb") as emp:
    rrhh = re.empleados
    write = pickle.dump(rrhh, emp)

def f():
    with open ("empleados.bin", "rb") as emp:
        file = pickle.load(emp)
        for record in file:
            for element in record:
                for e in record[element]:
                    print(f"{e} : {record[element][e]}")

with open ("empleados.bin", "rb") as emp: #   Factor de Suma de salarios, para saber el total de nomina
    file = pickle.load(emp)
    sum = 0
    for id in file:
        for DataEmploy in id: # dentro del id
            registro = id[DataEmploy]
            for elemento in registro:
                sueldo = registro["salario"]
            sum = sum + sueldo
    print(f"Total de nomina = {sum}")

# si se escribe el id que aparezca la lista al que corresponde


# Crea un archivo binario llamado "productos.bin" que contenga una lista de productos 
# de una tienda. Cada producto debe tener un código de barras único, nombre, precio, 
# cantidad en inventario y categoría. Escriba un programa que lea el archivo y muestre 
# la información de todos los productos con un inventario de menos de 10 unidades.

# Crea un archivo binario llamado "estudiantes.bin" que contenga una lista de estudiantes 
# de una escuela. Cada estudiante debe tener una matrícula única, nombre, apellido, edad, 
# curso y calificación final. Escriba un programa que lea el archivo y muestre la información 
# de todos los estudiantes que hayan aprobado (calificación mayor o igual a 70).

# Crea un archivo binario llamado "facturas.bin" que contenga una lista de facturas de una 
# empresa. Cada factura debe tener un número de factura único, nombre del cliente, fecha 
# de emisión, monto total y estado (pagado o pendiente). Escriba un programa que lea el 
# archivo y muestre la información de todas las facturas pendientes.