import dataBaseEdu as db #
import struct            
import pickle
import json




# with open("estudiantes.csv", "w") as clase:
#     contador = 0
#     for elemento in db.estudiantes:
#         contador = contador + 1
#         clase.writelines("\n")
#         clase.writelines("ESTUDIANTE " + str(contador) + "\n")
#         clase.writelines("\n")
#         for sub in elemento:
#             clase.writelines(sub + " : " + str(elemento[sub]) + "\n")

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
        lista_base = db.empleados
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
        lista = db.lista_productos
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
        ls = db.personas
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
        persons = db.personas
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
        estudiantes = db.estudiantes
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
        employees = db.empleados
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
        catalog = db.lista_productos
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




#_________________________________________________________________________________________________________
# Crea un archivo binario llamado "empleados.bin" que contenga una lista de empleados de 
# una empresa. Cada empleado debe tener un número de identificación único, nombre, edad, 
# género y puesto de trabajo. Escriba un programa que lea el archivo y muestre toda la 
# información de cada empleado.
def f():
    with open("empleados.bin", "wb") as emp:
        rrhh = db.empleados
        write = pickle.dump(rrhh, emp)


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

    with open ("empleados.bin", "rb") as emp: # si se escribe el id que aparezca la lista al que corresponde
        file = pickle.load(emp)
        buscador = int(input("Employee Code = "))
        for ids in file:
            for line in ids:
                id = ids[line]
                if line == buscador:
                    for element in id:
                        print (f"{element} : {id[element]}")

#_________________________________________________________________________________________________________
# Crea un archivo binario llamado "productos.bin" que contenga una lista de productos 
# de una tienda. Cada producto debe tener un código de barras único, nombre, precio, 
# cantidad en inventario y categoría. Escriba un programa que lea el archivo y muestre 
# la información de todos los productos con un inventario de menos de 10 unidades.
#_________________________________________________________________________________________________________

def f():
    with open("producto.bin", "wb") as product:
        write = pickle.dump(db.lista_productos, product)

    with open("producto.bin", "rb") as product:
        file = pickle.load(product)
        
        print("CODIGO DE CADA PRODUCTO\n") # imprime el codigo de cada producto.
        for ids in file:
            for code in ids:
                id = ids[code]
                name = id["nombre"]
                print(f"{name} = {code} \n")
        
        input = int(input("intruduzca el codigo = \n")) #  Se imprime un producto al introducir su codigo.
        for ids_ in file:
            for code_ in ids_:
                id_ = ids_[code_]
                if input == code_:
                    for element in id_:
                        print(f"{element} : {id_[element]}")

        for ids in file: #programa que imprime los elementos que tienen menos de 10 unidades.
            for code in ids:
                id = ids[code]
                warehouse = id["cantidad disponible"]
                if warehouse < 10:
                    for element in id:
                        print (f"{element} : {id[element]}")

#_________________________________________________________________________________________________________
# Crea un archivo binario llamado "estudiantes.bin" que contenga una lista de estudiantes 
# de una escuela. Cada estudiante debe tener una matrícula única, nombre, apellido, edad, 
# curso y calificación final. Escriba un programa que lea el archivo y muestre la información 
# de todos los estudiantes que hayan aprobado (calificación mayor o igual a 70).
#_________________________________________________________________________________________________________

def f():
    with open("estudiantes.bin", "wb") as archive:
        pickle.dump(db.estudiantes, archive)

    with open("estudiantes.bin", "rb") as archive:
        file = pickle.load(archive)
        
        promedios = []
        
        for ids0 in file:
            contador = 0
            for id0 in ids0:
                reg0 = ids0[id0] # El interior de las matriculas
                #print(reg0)
                sum = 0
                for base in reg0:
                    vaule = reg0[base]
                    #print(base)
                    if isinstance(vaule, int): # isinstance(objeto, clase) #Comprobar que objeto sea de una clase especifica
                        sum += vaule
                contador += 1
                #print (sum)
                prom = round(sum/3)
                result = prom * 4 / 100
                promedios.append(result) 
        #print(promedios)

        for ids in file:
            for id in ids:
                reg = ids[id]
                #print(reg["nombre"] ,reg["examen 1"])
                #for element in reg:
                    
                    #if reg[element] > 70:
                        #print 
                    
def f():
    with open("estudiantes.bin", "wb") as archive:
            pickle.dump(db.EstudiantesIndex, archive)

    with open("estudiantes.bin", "rb") as archive:
        file = pickle.load(archive)
        input = input(" Matricula = ")
        for element in file:
            data = file[element]
            #print(file[element])
            if element == input:
                for e in data:
                    print(f"{e} : {data[e]}")
#_________________________________________________________________________________________________________
# Crea un archivo binario llamado "facturas.bin" que contenga una lista de facturas de una 
# empresa. Cada factura debe tener un número de factura único, nombre del cliente, fecha 
# de emisión, monto total y estado (pagado o pendiente). Escriba un programa que lea el 
# archivo y muestre la información de todas las facturas pendientes.
#_________________________________________________________________________________________________________



#_________________________________________________________________________________________________________
#Crea un programa que lea un archivo de texto y lo convierta en un archivo indexado. El archivo de texto debe 
# tener una lista de nombres y edades separados por una coma. Cada línea del archivo debe tener un registro 
# diferente. El archivo indexado debe tener índices que apunten a cada registro del archivo de texto.
#_________________________________________________________________________________________________________

def empleados():
    archive_bin = "EmpleadosTec_No_Index.bin"
    with open(archive_bin, "wb") as archive:
        stafs = db.empleadosNU
        pickle.dump(stafs, archive)
    indice = {}
    def Read_Archive(archive_bin):
        with open(archive_bin, "rb") as archive:
            file = pickle.load(archive)
            
            for i, data in enumerate(file):
                indice[data["nombre"]] = i

            NewRegitry = {}
            for regitry, id in zip(file, indice):
                NewRegitry[id] = regitry
            
        with open("EmpleadosTec_Index.bin", "wb") as no_index:
            pickle.dump(NewRegitry, no_index)
        with open("EmpleadosTec_Index.bin", "rb") as no_index:
            readFile = pickle.load(no_index)
            for frame in readFile:
                print(f"{frame} : {readFile[frame]} \n")
    Read_Archive(archive_bin)




#_________________________________________________________________________________________________________
#Crea una función que lea un archivo indexado y muestre el nombre y el puesto de los empleados que tienen 
# más de 5 años de experiencia en la empresa.
#_________________________________________________________________________________________________________

def ReadIndex():
    with open("EmpleadosTecIndex.txt", "rb") as archive:
        read = archive.readlines()
        for line in read:
            print (line)
            #for ids in line:
                #print(ids)

#_________________________________________________________________________________________________________
#Crea un programa que lea un archivo de texto y lo convierta en un archivo indexado. El archivo de texto 
# debe tener una lista de nombres, edades y direcciones separados por una coma. Cada línea del archivo 
# debe tener un registro diferente. El archivo indexado debe tener índices que apunten a cada registro 
# del archivo de texto y permitan acceder a los datos de cada persona.
#_________________________________________________________________________________________________________
def Text():
    with open("Lista_Dominicanos.txt", "w") as archive:
        Do = db.dominicanos
        for line in Do:
            archive.writelines(str(line) + "\n")

archive_DO = "Lista_Dominicanos.txt"

def Index(archive_DO):
    index = {}
    contador = 0
    with open(archive_DO, "r") as archive:
        read = archive.readlines()
        for line in read:
            element = line.strip()
            index[contador] = element
            contador += 1
        with open (archive_DO, "w") as archivex:
            for ind, record in index.items():
                archivex.writelines(str(ind) + ": " + str(record) + "\n")

#_________________________________________________________________________________________________________
#Crea un programa que lea un archivo de texto y lo convierta en un archivo indexado. El archivo de texto 
# debe tener una lista de nombres, salarios y puestos de trabajo separados por una coma. Cada línea del 
# archivo debe tener un registro diferente. El archivo indexado debe tener índices que apunten a cada 
# registro del archivo de texto y permitan acceder a la información de cada empleado.
#_________________________________________________________________________________________________________

def Create_Archive_Without_Key():
    with open("Registros_empleados_2022.txt", "w") as archive:
        record = db.empleadosNU
        for count,info in enumerate(record):
            final_record = count == len(record) - 1 
            for count2, atributte in enumerate(info):
                clave = str(atributte)
                valor = str(info[atributte])
                final_info = count2 == len(info) - 1
                if final_info and final_record:           
                    archive.write(clave +" : "+ valor)
                else:
                    archive.write(clave +" : "+ valor + ", ")
            if final_record:
                return
            archive.write("\n")

record_employee = "Registros_empleados_2022.txt"
def Index2(record_employee):
    index = {}
    with open(record_employee, "r") as archive:
        read = archive.readlines()
        for count ,line in enumerate(read):
            linea = line.strip().split()
            index[count] = linea
        with open(record_employee, "w") as archive:
            for element in index:
                clave = str(element)
                valor = str(index[element])
                archive.writelines(clave + ": " + valor + "\n")


#_________________________________________________________________________________________________________
#Crea un programa que lea un archivo de texto y lo convierta en un archivo indexado. El archivo de texto 
# debe tener una lista de peliculas separados por una coma. Cada línea del archivo debe tener un registro 
# diferente. El archivo indexado debe tener índices que apunten a cada registro del archivo de texto y 
# permitan acceder a la información de cada empleado.
#_________________________________________________________________________________________________________

def Create_Archive_Without_Key2():
    with open("peliculas_.txt", "w") as archive:
        movie = db.movie2
        for count, record in enumerate(movie):
            final_record = count == len(movie) - 1
            for count2 ,atributte in enumerate(record):
                for count3 ,element in enumerate(atributte):
                    final_element = count3 == len(atributte) - 1
                final_atributte = count2 == len(record) - 1
                conjunt = str(atributte) + ": " +  str(record[atributte])
                if final_element & final_atributte:
                    archive.writelines(conjunt)
                else:
                    archive.writelines(conjunt + ", ")
            if final_record:
                return
            else:
                archive.writelines("\n")
#Create_Archive_Without_Key2()
def Create_Archive_Without_Key3():
    with open("Pelicula_n.txt", "w") as archive:
        movies = db.movie2
        for movie in movies:
            archive.writelines(str(movie) + "\n")
#Create_Archive_Without_Key3()

movie = "peliculas_.txt"
movie2 = "Pelicula_n.txt"

def Index3(movie):
    index = {}
    with open(movie, "r") as archive:
        read = archive.readlines()
        for count, line in enumerate(read):
            linea = line.strip()
            index[count] = linea
        with open(movie, "w") as archive:
            for element in index:
                conjunt = str(element) + ": " + str(index[element])
                archive.writelines(conjunt + "\n")
#Index3(movie)

#_________________________________________________________________________________________________________
#Crea un programa que permita agregar, eliminar y modificar registros en un archivo indexado creado 
# en el ejercicio anterior. El programa debe pedir al usuario el nombre y la edad del registro a 
# agregar, eliminar o modificar.

employee = "empleados.bin"

def Create_Archive_Bin(employee):
    with open(employee, "wb") as bin:
        employees = db.empleadosNU
        pickle.dump(employees, bin)
Create_Archive_Bin(employee)

def Read_Archive_Bin_and_Index(employee):
    index = {}
    arch_index = {}
    with open(employee, "rb") as bin:
        read = pickle.load(bin)
        for count, data in enumerate(read):
            index[data["nombre"]] = count
        with open(employee, "wb") as bin:
            for element, data in zip(index, read):
                arch_index[element] = data
            pickle.dump(arch_index, bin)
Read_Archive_Bin_and_Index(employee)

def Add_Del_Mod(employee):
    decide = "mod"
    pack = {}
    with open(employee, "rb") as bin:
        read = pickle.load(bin)
        lista = ["nombre","edad","puesto","tiempo_trabajando"]
        contador = 0
        box = {}
        for record in read:
            pack[record] = read[record]
        if decide == "add":
            for element in lista:
                contador += 1
                vaule = input(f"{element} = ")
                box[element] = vaule
            pack[box[lista[0]]] = box
            print (pack)
        elif decide == "del":
            switch = True
            delete = "sdcds"
            count = 0
            for line in read:
                count += 1
                if line == delete:
                    del pack[delete]
                    switch = False
            if switch == True:
                print ("Esta persona no esta en este record \n")
        elif decide == "mod":
            modify = "Juan"
            cont = 0
            for line in pack:
                intro = pack[line]
                # switch = True
                # while switch:
                element_mod = input("Atributo a modificar = ")
                if line == modify:
                    for i, atributte in enumerate(intro):
                        if element_mod == atributte:
                            vaule_element = input(f"{element_mod} = ")
                            condition = i == len(intro)
                            intro[element_mod] = vaule_element
                            break
                        cont += 1
                    if i == cont:
                        print("Incorrecto")
                    elif element_mod == "salir":
                        print ("algo")
                        break
                else:
                    break
                #print(intro)



#Add_Del_Mod(employee)
