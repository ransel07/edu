# EJERCICION PARA PRACTICAS DE ARREGLOS O LISTA

# Listas para usar en ejercicions:
lista_num10 = [1,2,3,4,5,6,7,8,9,10]
lista_enteros100 = []
for element in range(1, 100):
    lista_enteros100.append(element)


#arreglo1()

#Crea un arreglo que contenga los números pares del 2 al 20 y 
# muestra en pantalla la suma de todos los elementos del arreglo.

def suma_lista():
    lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print(sum(lista))

def suma_nueva(lista):
    suma = sum(lista)
    print(suma)


suma_lista()
suma_nueva(lista_enteros100)

#Crea un arreglo que contenga los números impares del 1 al 19 y 
# muestra en pantalla el producto de todos los elementos del arreglo.

def producto_lista():
    lista = [1,3,5,7,9,11,13,15,17,19]
    producto = 1
    for elemento in lista:
        producto = producto * elemento
    print(producto)

#producto_lista()

#Crea un arreglo que contenga los nombres de los días de la semana y 
# muestra en pantalla el nombre del día que ocupa la posición 4 en el arreglo.

def dia():
    lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    print(lista[3])
#dia()

#Crea un arreglo que contenga las vocales del alfabeto y 
# muestra en pantalla la posición en el arreglo de la vocal "a"

def bocales():
    lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    cont = 0
    for elemento in lista:
        if elemento == "a":
            print(cont)
        cont = cont + 1

#bocales()

#Crea un arreglo que contenga los números del 1 al 10 
# en orden aleatorio y muestra en pantalla el arreglo ordenado de menor a mayor.

def arreglo_ordenado():
    lista = [1,2,3,4,5,6,7,8,9,10]
    for element in lista:
        print(element)

#arreglo_ordenado()

#Crea un arreglo que contenga los números del 1 al 10 y luego agrega el número 11 al 
# final del arreglo y muestra en pantalla el contenido del arreglo.

def elemento_11():
    lista = [1,2,3,4,5,6,7,8,9,10]
    lista.append(11)
    print(lista[10])

#elemento_11()

#Crea un arreglo que contenga los números del 1 al 10 y luego elimina el número 5 
# del arreglo y muestra en pantalla el contenido del arreglo.

def eliminacion():
    lista = [1,2,3,4,5,6,7,8,9,10]
    lista.pop(4)
    print(lista)

#eliminacion()

#Crea un arreglo que contenga los números del 1 al 10 y luego busca el número 7 en 
# el arreglo y muestra en pantalla si se encuentra o no en el arreglo.

def arreglo():
    lista = [1,2,3,4,5,6,7,8,9,10]
    for element in lista:
        if element == 7:
            print('Se encuentra 7 en el arreglo')
            return
        
    print("No se encuentra este elemento en el arreglo")

#arreglo()

#Dado un array de números enteros, escriba una función que devuelva el número más grande y el más pequeño en el array.
def num_mayor_menor():
    lista = [1,2,3,4,5,6,7,8,9,10]
    num_mayor = max(lista)
    num_menor = min(lista)
    print(num_mayor, num_menor)

#num_mayor_menor()

#Dado un array de strings, escriba una función que devuelva un nuevo array que contenga todas las strings en mayúsculas.

def strings_arreglo():
    lista = ["klk", "tu", "dice", "mio"]
    for string in lista:
        string.upper()
        print(string.upper())

#strings_arreglo()

#Dado un array de números enteros, escriba una función que devuelva un nuevo array que contenga solo los números pares del array original.

def pares():
    lista = [1,2,3,4,5,6,7,8,9, 10]
    array_par = []
    array_par = []
    for num in lista:
        if num % 2 == 0:
            array_par.append(num)
    print(array_par)

#pares()

#Dado un array de números enteros, escriba una función que devuelva la suma de todos los números en el array.

def sum_enteros():
    lista = [1,3,5,7,9,11,13,15,17,19]
    sum = 0
    for num in lista:
        sum = sum + num
    print(sum)

#sum_enteros()

#Dado un array de strings, escriba una función que devuelva un nuevo array que contenga solo las strings que comiencen con la letra "a".

def a_strings():
    series = ["Andor", "House of the Dragon", "Lord of the Ring", 
                "Boku No Hero Academia", "American Horror Story"]
    series_a = []
    for una_serie in series:
        primer_caracter = una_serie[0]   # El primer caracter de "una_serie".
        if primer_caracter == "A":       
            series_a.append(una_serie)   # Coloco en el array "serie_a" una "una_serie" por cada ciclo del bucle.
    print(series_a)
#a_strings()

# 5.10 Dado un array de números enteros, devuelve un nuevo array donde cada elemento es el resultado de multiplicar el elemento 
# del array original por su índice. Por ejemplo, dado el array [2, 3, 1, 0], debería devolver [0, 3, 2, 0].

def devolucion_indice():
    array_original = [1, 2, 3, 2, 1, 3, 3]
    indice = 5
    nuevo_array = []
    for num in array_original:
        potencia = num ** indice
        nuevo_array.append(potencia)
    print (nuevo_array)
#devolucion_indice()

#Parte Buena del ejercicio
def multiply_by_index(numbers):
    result = []
    for elemento in range(len(numbers)):
        result.append(numbers[elemento] * elemento)
    return result

# prueba el código con algunos ejemplos 
#print(multiply_by_index([2, 3, 1, 0]))  # debería imprimir [0, 3, 2, 0]
#print(multiply_by_index([-1, 0, 1, 2, 3]))  # debería imprimir [0, 0, 2, 6, 12]
#print(multiply_by_index([1, 2, 3, 4, 5]))  # debería imprimir [0, 2, 6, 12, 20]


# 5.11 Dado un array de cadenas de caracteres, devuelve un nuevo array donde todas las palabras que comiencen con la letra "a" o 
# "A" se convierten a mayúsculas. Por ejemplo, dado el array ["apple", "banana", "Almond"], debería devolver ["APPLE", "BANANA", "ALMOND"].

def a_strings():
    series = ["Andor", "House of the Dragon", "Lord of the Ring", 
                "Boku No Hero Academia", "American Horror Story"]
    nuevo_array = []
    for una_serie in series:
        primer_caracter = una_serie[0]      
        if primer_caracter == "A":       
            nuevo_array.append(una_serie)   
        elif primer_caracter == "a":
            nuevo_array.append(una_serie)
    print(nuevo_array)
#a_strings()

# 5.12 Dado un array de números enteros, devuelve el número que se repite más veces en el array. Si ningún número se repite, 
# debería devolver cero. Por ejemplo, dado el array [1, 2, 3, 2, 1, 3, 3], debería devolver 3.

def num_repit(lista_num):
    caja = []
    for elemento in lista_num:
        contador = lista_num.count(elemento)  # El metodo "count()" devuelve la cantidad de veces que se repite un elemento en una lista_num
        caja.append(contador)                 # El metodo "append()" introduce un numero especifico en una lista_num
    numero_mayor = max(caja)               
    posicion = caja.index(numero_mayor)       # El método "index()" devuelve la posición del primer elemento que coincide con el valor que se busca.
    
    if lista_num[posicion] > 1:               # El resultado de "lista_num[posicion] = 1" si no hay numero que se repitan, por lo tanto se realiza esta condicional 
        print(lista_num[posicion])
    else:
        print(0)

#num_repit(lista_num10)

