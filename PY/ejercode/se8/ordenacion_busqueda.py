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
"___________________________________________________"

def Quicksort_lista_listas(lista, count):
    if count < 1:
        array = [sum(interlist) for interlist in lista]
    count += 1
    if len(array) < 2:
        return array

    pivot = array[0]
    left = [element for element in array if element <= pivot]
    right = [element for element in array if element > pivot]

    print (f"{left}, {pivot}, {right}")

    less = Quicksort_lista_listas(left, count)
    more = Quicksort_lista_listas(right, count)
    return less + pivot + more + count

count = 0
lista_in_lista = [[23,12], [23,13], [42,43], [32, 22]]
i = Quicksort_lista_listas(lista_in_lista, count)
print (i)