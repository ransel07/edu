# Crea un arreglo que contenga los números del 1 al 10 y 
# muestra en pantalla cada uno de los elementos del arreglo.

#variable_generica 

def arreglo1():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print(lista)

#arreglo1()

#Crea un arreglo que contenga los números pares del 2 al 20 y 
# muestra en pantalla la suma de todos los elementos del arreglo.

def suma_lista():
    lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print(sum(lista))

#suma_lista()

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

a = [[1, 2, 3], 
    [4, 5, 6],
    [6,4,4]]

for fragmentos in a:
    producto_01 = 0
    elements_01 = a[0] * a[4] * a[8]
    elements_02 = [a[1], a[5], a[6]]
    elements_03 = [a[0], a[4], a[8]]



    print (elements_01)
