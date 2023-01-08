import dataBaseEdu as db
from colorama import Fore, Style

def f():
    def intercambion(lista):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

    lista = [5, 2, 8, 1, 4]
    intercambion(lista)
    print(lista)


def quicksort(lista):
    if len(lista) < 2:
        return lista
    
    pivote = lista[0]

    left = [num for num in lista[1:] if num <= pivote]
    
    right = [num for num in lista[1:] if num > pivote]
    
    # print(f"{left}, {pivote}, {right}")
    
    return quicksort(left) + [pivote] + quicksort(right)

# lista = [9,34,6,4,43,35,5,63,12,1,7,46,16,15,12,23,1,11,4,13,74,3,8,3,4,14,43,30]
# oredemado = quicksort(lista)
# print (oredemado)

"________________________________________________________________________________"
"Ordena la lista de mayor a menor"
"________________________________________________________________________________"

def quicksort_right(lista):
    if len(lista) < 2:
        return lista
    
    pivote = lista[len(lista) - 1]

    left = [num for num in lista[:-1] if num >= pivote]
    right = [num for num in lista[:-1] if num < pivote]

    # print(f"{left}, {pivote}, {right}")

    return quicksort_right(left) + [pivote] + quicksort_right(right)

# oredemado1 = quicksort_right(lista)
# print (oredemado1)


"________________________________________________________________________________"
"Ordena lista alfabeticamente"
"________________________________________________________________________________"



def ordenacion_arf(cadenas):
    if len(cadenas) < 1:
        return cadenas
    
    pivote = cadenas[0]

    left = [caracter for caracter in cadenas[1:] if caracter.lower() < pivote.lower()]
    
    right = [caracter for caracter in cadenas[1:] if caracter.lower() >= pivote.lower()]
    
    # print(f"{left}, {pivote}, {right}")
    
    return ordenacion_arf(left) + [pivote] + ordenacion_arf(right)

cademas = ["cadena", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo", "arbusto"]
oredemado_alf = ordenacion_arf(cademas)

# print (oredemado_alf)

"___________________________________________________"
"ordenar lista de caracteres deacuerda a su longitud"
"___________________________________________________"

def Quicksort_Caracteres_longitud(cadenas):
    if len(cadenas) <= 1:
        return cadenas
    
    pivot = cadenas[0]

    left = [cadena for cadena in cadenas[1:] if len(cadena) <= len(pivot)]
    right = [cadena for cadena in cadenas[1:] if len(cadena) > len(pivot)]

    print(f"{left}, {pivot}, {right}")

    less = Quicksort_Caracteres_longitud(left)
    more = Quicksort_Caracteres_longitud(right)

    # return list(less) + list(pivot) + list(more)

cadenas = ["klk", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo", "arbusto"]
# oredemado_alf = Quicksort_Caracteres_longitud(cadenas)

# print (oredemado_alf)

"___________________________________________________"
"ordenar lista de listas de números de acuerdo a la suma de"
"sus elementos (de mayor a menor)"
"____________________________________________________________"

def Quicksort_Suma_listas(lista, count):
    if len(lista) <= 1:
        return lista
    
    if count < 1:
        lista = [sum(element) for element in lista]

    pivot = lista[0]
    
    left = [element for element in lista[1:] if element <= pivot]
    right = [element for element in lista[1:] if element > pivot]

    print (f"{left}, {pivot}, {right}, {count}")
    count += 1

    less = Quicksort_Suma_listas(left, count)
    more = Quicksort_Suma_listas(right, count)
    return less + [pivot] + more

# count = 0
# lista_in_lista = [[23,12], [23,13], [42,43], [32, 22], [22, 21], [20, 15], [13, 10], [50, 55]]
# i = Quicksort_Suma_listas(lista_in_lista, count)
# print (i)

"____________________________________________________________"
"Crear una función que reciba una lista de palabras y devuelva una nueva "
"lista con las palabras en orden inverso."
"____________________________________________________________"

def QuickSort_inverse(lista):
    if len(lista) <= 1:
        return lista
    
    pivot = lista[0]

    left = [cadena for cadena in lista[1:] if cadena.lower() >= pivot.lower()]
    right = [cadena for cadena in lista[1:] if cadena.lower() < pivot.lower()]

    print (f"{left} {pivot} {right}")

    less = QuickSort_inverse(left)
    more = QuickSort_inverse(right)

    return less + [pivot] + more

# inv = QuickSort_inverse(db.list_cadenas)
# print (inv)

"______________________________________________________________________________"
"Crear una función que reciba una lista de nombres y devuelva una nueva lista "
"con los nombres en orden alfabético."
"______________________________________________________________________________"

def QuickSort_Names_Alphbert(lista):
    if len(lista) <= 1:
        return lista
    
    pivot = lista[0]

    left = [name for name in lista[1:] if name.lower() <= pivot.lower()]
    right = [name for name in lista[1:] if name.lower() > pivot.lower()]

    print (f"{left}{pivot}{right}")

    less = QuickSort_Names_Alphbert(left)
    more = QuickSort_Names_Alphbert(right)

    return less + [pivot] + more

# names = QuickSort_Names_Alphbert(db.list_names)
# print (names)
"______________________________________________________________________________"
"Dadas dos listas de números, implementa una función que devuelva una lista que contenga "
"todos los números de ambas listas, ordenados de menor a mayor."
"______________________________________________________________________________"

def QuickSort_Combinacion_Listas(lista, lista2):
    klk = len(lista)
    for num in lista2:
        lista.append(num)
    
    def QuickSort(lista):
        if len(lista) <= 1:
            return lista
        
        pivot = lista[0]

        left = [e for e in lista[1:] if e <= pivot]
        right = [e for e in lista[1:] if e > pivot]

        print (f"{left}{pivot}{right}")

        return QuickSort(left) + [pivot] + QuickSort(right)
    qs = QuickSort(lista)
    return qs
# qcl = QuickSort_Combinacion_Listas(db.list_num, db.list_num2)
# print (qcl)

"______________________________________________________________________________"
"Dados dos archivos de texto con palabras, implementa una función que devuelva un archivo "
"de texto que contenga todas las palabras de ambos archivos, ordenadas alfabéticamente."
"______________________________________________________________________________"

def Archives_(file, file2):
    with open(file, "w") as archive1:
        count = 0
        for line in db.words_list_:
            if count <= 10:
                archive1.writelines(line + ", ")
                count += 1
            else:
                archive1.writelines(line + "\n")
                count = 0
    with open(file2, "w") as archive1:
        count = 0
        for line in db.words_list_2:
            if count <= 10:
                archive1.writelines(line + ", ")
                count += 1
            else:
                archive1.writelines(line + "\n")
                count = 0


# Archives_(file, file2)

def QuickSort_Archives_Alphabet(file, file2):
    final_list = []
    with open(file, "r") as archive:
        read = archive.readlines()
        for line in read:
            line_list = line.split()
            for element in line_list:
                final_list.append(element)
    with open(file2, "r") as archive2:
        read = archive2.readlines()
        for line2 in read:
            line_list2 = line2.split()
            for element2 in line_list2:
                final_list.append(element2)
    print (len(final_list))
    def QuickSort(lista):
        if len(lista):

file = "archive1.txt"
file2 = "archive2.txt"
QuickSort_Archives_Alphabet(file, file2)
