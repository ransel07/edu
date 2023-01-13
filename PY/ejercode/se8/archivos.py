from colorama import Fore, Style
import dataBaseEdu as bd

def Archive_CSV_MySQL(archivo):
    with open(archivo, "w") as csv:
        employee = bd.empleadosNU
        count = 0
        for line in employee:
            for renglon in line:
                count += 1
                key = str(renglon)
                value = str(line[renglon])
                if count < len(line):
                    csv.writelines(key + ", " + value + ", ")
                else:
                    csv.writelines(key + ", " + value)
                    count = 0
            csv.writelines("\n")

# archivo = "employees.csv"
# Archive_CSV_MySQL(archivo)

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



def funsion():
    with open("ejercicio6.txt", "w") as e6:
        for elemento in bd.libros_titulo1:
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
        for elemento in bd.empleados:
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


def CreateTex():
    with open("productos.txt", "w") as productos:
        contar = 0
        for elemento in bd.lista_productos:
            visual = "---------------- " + elemento["nombre"] + " ----------------\n"
            code = "codigo del producto " + str(contar)
            productos.writelines(" \n" + visual)
            productos.writelines(str(code) + " \n")
            for sub in elemento.keys():
                productos.writelines(str(sub) + " : " + str(elemento[sub]) + "\n")

            contar = contar + 1
    with open ("productos.txt", "r") as productos:
        lineas = productos
        for linea in lineas:
            print(linea)
#CreateTex()

def BuyProduct():
    print ("ARTICULOS DE PC")
    print (" ")

    buy = int(input("Codigo del producto = "))
    cant_buy = int(input("Cantidad = "))

    if 0 <= buy <= 7:
        prod= bd.lista_productos[buy]    # Obtener el producto con índice 0
        # Acceder a la propiedad "cantidad disponibles" del producto
        cantidad_disponible = prod["cantidad disponible"]
        p = int(cantidad_disponible)  - int(cant_buy)
        print (p)
    else:
        print("Este articulo no existe ")

#BuyProduct()

# Crea un archivo de texto que contenga información sobre diferentes estudiantes 
# y sus calificaciones en un curso (nombre, notas en cada examen, promedio final, 
# etc.). Luego, escribe un programa en Python que lea el archivo y muestre la 
# lista de estudiantes ordenada por promedio final.

def PromedioFinalx():
    with open("estudiantes.csv", "w") as clase:
        contador = 0
        for elemento in bd.estudiantes:
            contador = contador + 1
            clase.writelines("\n")
            clase.writelines("ESTUDIANTE " + str(contador) + "\n")
            clase.writelines("\n")
            for sub in elemento:
                clase.writelines(sub + " : " + str(elemento[sub]) + "\n")
    with open("estudiantes.csv", "r") as es:

        caja = es.readlines()
        titulo = 1
        nombre = 3
        desarrollo = 8
        while desarrollo <= 48:
            print(caja[titulo])
            print(caja[nombre])
            print(caja[desarrollo])
            titulo += 10
            nombre += 10
            desarrollo += 10
# PromedioFinalx ()


# Crea un archivo de texto con información sobre diferentes estudiantes y sus 
# calificaciones en un curso (nombre, notas en cada examen, promedio final, etc.). 
# Luego, escribe un programa en Python que lea el archivo y almacene la información 
# de cada estudiante en un registro. Utiliza un arreglo de estos registros para 
# luego mostrar la lista de estudiantes ordenada por promedio final.

def PromedioFinal2():
    with open("estudiates2.txt", "w") as promedio2:
        lista = bd.estudiantes
        for line in lista:
            promedio2.writelines(str(line) + "\n")
    with open("estudiantes2.txt", "r") as WrithProm:
        escritura = WrithProm.writelines()
        
#PromedioFinal2()
"______________________________________________________________________________________"
"Crea un archivo de texto con información sobre diferentes productos en una tienda" 
"(nombre, precio, cantidad disponible, etc.). Luego, escribe un programa en Python" 
"que lea el archivo y almacene la información de cada producto en un registro." 
"Utiliza un arreglo de estos registros para luego permitir al usuario buscar un "
"producto específico por nombre y mostrar toda su información."
"______________________________________________________________________________________"

arch_article = "productos2.txt"

def producto2(arch_article):
    with open(arch_article, "w") as archive:
        l_productos = bd.productos
        for record in l_productos:
            for i, atributte in enumerate(record):
                count = i < len(record) - 1
                key = str(atributte)
                vaule = str(record[atributte])
                if count:
                    archive.writelines(key + " : " + vaule + ", ")
            archive.writelines(key  + " : " + vaule + "\n")
    
    with open(arch_article, "r") as articulo:
        read = articulo.readlines()

        def Organization(read):
            temporary = {}
            pack = []
            for line in read: 
                division = line.strip().split(",")
                for element in division:
                    division1 = element.strip().split(":")
                    temporary[division1[0].strip()] = division1[1].strip()
                    if element.startswith(" c"):
                        pack.append(temporary)
                        temporary = {}
            return pack
        org = Organization(read)

        def available(org):
            print(" ")
            print(Fore.BLUE + "-----------Articulos disponibles-----------\n" + Style.RESET_ALL)
            for record3 in org:
                for keys in record3:
                    if keys == "nombre":
                        articule_color = Fore.RED + record3[keys] + " " + record3["marca"] + Style.RESET_ALL
                        print (articule_color)
            return "-----------------"
        brochure = available(org)
        print (brochure)

        print(" ")
        print(Fore.GREEN + "OBTEN DATOS DEL ARTICULO QUE NESECITAS \n" + Style.RESET_ALL)
        def Select(org):
            while True:
                count = 0
                intro = "Consultar" #input("Que quieres hacer? ").title()
                if intro == "Salir":
                    return print(Fore.YELLOW + "Gracias por visitarnos" + Style.RESET_ALL)
                elif intro == "Consultar":
                    name = "laptop" #input("Nombre del articulo: ").title()
                    trademark = "HP" #input("Marca: ").title()
                    for record in org:
                        atributte1 = record["nombre"] == name.title()
                        atributte2 = record["marca"] == trademark.title()
                        if atributte1 and atributte2:
                            count += 1
                            for atributte3 in record:
                                print (f"|{atributte3}|{record[atributte3]}|")
                else:
                    print ("Accion a realizar no valida \n")
                if count < 0:
                    print (f"El articulo {name} {trademark} no pertenece a la lista proporcionada")
        Select(org)

# producto2(arch_article)

"______________________________________________________________________________________"
"Crea un archivo de texto con información sobre diferentes empleados de una empresa "
"(nombre, cargo, salario, etc.). Luego, escribe un programa en Python que lea el archivo" 
"y almacene la información de cada empleado en un registro. Utiliza un arreglo de estos" 
"registros para luego calcular el salario total de todos los empleados y mostrar el" 
"promedio de salarios por cargo."
"______________________________________________________________________________________"

archive ="employe.txt"

def info_empploye(archive):
    with open(archive, "w", encoding = 'utf-8') as arch:
        empploye = bd.empleadosNU
        for line in empploye:
            for element in line:
                vaule = str(line[element])
                key = str(element)
                arch.writelines(key + " : " + vaule + "\n")
    
    with open(archive, "r") as arch:
        read = arch.readlines()

        def organizacion(read):
            array = []
            record = {}
            for line in read:
                nline = line.strip().split(":")
                record[nline[0]] = nline[1]
                if line.startswith("t"):
                    array.append(record)
                    record = {}
            return array
        array = organizacion(read)

        def puesto_salario(array):
            bridge = {}
            for dict in array:
                bridge[dict["puesto "]] = int(dict["salario "])
            return bridge
        result = puesto_salario(array)

        def average(result):
            avg = {}
            for key, vaule in result.items():
                if key in avg:
                    avg[key] = (avg[key] + vaule) / 2
                else:
                    avg[key] = vaule
            return avg
        print(average(result))

# info_empploye(archive)

"________________________________________________________________________________________"
"Crea un archivo de texto con información sobre diferentes libros (título, autor, año de" 
"publicación, etc.). Luego, escribe un programa en Python que lea el archivo y almacene" 
"la información de cada libro en un registro. Utiliza un arreglo de estos registros para" 
"luego permitir al usuario buscar libros por año de publicación y mostrar todos los" 
"títulos y autores de los libros publicados en ese año."
"________________________________________________________________________________________"

def f():
    def quicksort(lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        mayores = [x for x in lista[1:] if x >= pivote]
        print (f"{menores}{pivote}{mayores}")
        return quicksort(menores) + [pivote] + quicksort(mayores)

    with open('archivo.txt', "w", encoding = 'utf-8') as arch:
        nums = bd.list_num
        for i, num in enumerate(nums):
            if i < len(nums) - 1:
                arch.writelines(str(num) + ", ")
            else:
                arch.writelines(str(num))

    with open('archivo.txt', 'r', encoding = 'utf-8') as f:
        line = f.readlines()
        new_list = []
        for numb in line:
            box = numb.split()
            for element in box:
                inc = element.strip(", ")
                new_list.append(int(inc))
        print(new_list)

    lista = quicksort(new_list)

    with open('archivo.txt', "w", encoding = 'utf-8') as f:
        for i, n in enumerate(lista):
            if i < len(lista) - 1:
                f.writelines(str(n) + ", ")
            else:
                f.writelines(str(n))


"Crea un progama que lea un archivo de texto con palabras separados por coma,"
"los guarde en una lista y los ordene alfabeticamente usando el algoritmo de quicksort."
"Escriba el resultado ordenado en un nuevo archivo."

def Write_Archive_Word(archive):
    with open(archive, "w", encoding= "utf-8") as file:
        words = bd.words_list_2
        for count, word in enumerate(words):
            if count < len(words) - 1:
                file.writelines(str(word) + ", ")
            else:
                file.writelines(str(word))

archive = "archivo_palabras_desordenadas.txt"

def Read_Archive_Words(archive):
    with open(archive, "r", encoding= "utf-8") as file:
        read = file.read()
        box = []
        separate = read.split(",")
        for element in separate:
            box.append(element.strip())
        print(f"Sin organizar: {box}")
        
        def QuickSort(box):
            if len(box) <= 1 :
                return box
            pivot = box[0]
            left = [word for word in box if word.lower() <= pivot.lower()]
            right = [word for word in box if word.lower() > pivot.lower()]
            return QuickSort(left) + [pivot] + QuickSort(right)
        result = QuickSort(box)
        print (f"Organizado alfabeticamente: {result}")
archive = "archivo_palabras_desordenadas.txt"
rd = Read_Archive_Words(archive)

print (rd)