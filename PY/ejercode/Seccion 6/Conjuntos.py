#EJERCICOS BASICO DE CONJUNTOS

#Crea un conjunto con los números enteros del 1 al 10 y guarda su resultado en una variable llamada conjunto_1. Imprime el resultado en pantalla.

conjunto_1 = {1,2,3,4,5,6,7,8,9,10}

#print(conjunto_1)

#Crea un conjunto con los números pares del 1 al 10 y guarda su resultado en una variable llamada conjunto_2. Imprime el resultado en pantalla.

conjunto_2 = {1,2,3,4,5,6,7,8,9,10}
conjunto_22 = list(conjunto_2)
for num in conjunto_22 :
    print(conjunto_22)

# Utiliza el método intersection() para encontrar los elementos que están presentes en ambos conjuntos conjunto_1 y conjunto_2. 
# Imprime el resultado en pantalla.

elem_comun = conjunto_2.intersection(conjunto_1)

#print(elem_comun)

# Utiliza el método difference() para encontrar los elementos que están presentes en conjunto_1 pero no en conjunto_2. Imprime el resultado en pantalla.

elem_diferentes = conjunto_2.difference(conjunto_1)

#print(elem_diferentes)

# Utiliza el método union() para combinar los elementos de ambos conjuntos conjunto_1 y conjunto_2. Imprime el resultado en pantalla.

unificacion = conjunto_2.union(conjunto_1)

#print(unificacion)

# Crea un conjunto con los números del 1 al 10 y guarda su resultado en una variable llamada conjunto_1. Luego, crea un conjunto con los 
# números del 5 al 15 y guarda su resultado en una variable llamada conjunto_2.

conjunto_1 = {1,2,3,4,5,6,7,8,9,10}
conjunto_2 = {5,6,7,8,9,10,11,12,13,14}

# Utiliza el método add() para agregar un nuevo elemento al conjunto conjunto_1. Imprime el resultado en pantalla para verificar que el 
# elemento se ha agregado correctamente.

conjunto_1.add(11)

#print(conjunto_1)

# Utiliza el método update() para agregar varios nuevos elementos al conjunto conjunto_2. Imprime el resultado en pantalla para verificar 
# que los elementos se han agregado correctamente.

num = [15,16,17,18,19,20]

conjunto_2.update(num)

#print(conjunto_2)

# Utiliza el método remove() para eliminar un elemento del conjunto conjunto_1. Imprime el resultado en pantalla para verificar que el 
# elemento se ha eliminado correctamente.

conjunto_1.remove(11)

#print(conjunto_1)

# Utiliza el método discard() para eliminar un elemento del conjunto conjunto_2. Imprime el resultado en pantalla para verificar que el 
# elemento se ha eliminado correctamente.

conjunto_2.discard(5)

#print(conjunto_2)

# Para trabajar con conjuntos en Python, puedes usar la clase set. A continuación te presento algunos ejercicios de nivel medio que puedes 
# resolver usando esta clase:

# Dado dos conjuntos A y B, crea un conjunto que contenga todos los elementos que pertenecen a A o a B, pero no a ambos. Para hacer esto, 
# puedes usar el método symmetric_difference de la clase set.
A = conjunto_1
B = conjunto_2

i = A.symmetric_difference(B) # Es decir, symmetric_difference elimina los que se repiten

#print(i)

# Dado un conjunto A, crea un nuevo conjunto que contenga todos los elementos de A, además de un nuevo elemento x. Para hacer esto, puedes 
# usar el método add de la clase set.

variable = 11

def añadir(num):
    A.add(num)
    print(A)

#añadir(variable)

# Dado un conjunto A, crea un nuevo conjunto que contenga todos los elementos de A, excepto el elemento x. Para hacer esto, puedes usar el 
# método discard de la clase set.

def eliminar_conj(num):
    A.discard(num)
    print(A)

#eliminar_conj(variable)

# Dado dos conjuntos A y B, determina si A es un subconjunto de B. Para hacer esto, puedes usar el método issubset de la clase set.
R = {4, 1, 3, 5}
S = {6, 0, 4, 1, 5, 0, 3, 5}

def subconjunto(x, y):
    if x.issubset(y) == True:
        print(y, "es un subconjunto de", x)
    elif y.issubset(x) == True:
        print("Al contrario", x, "es un subconjunto de", y)
    else:
        print("No existen subconuntos entre", x, "y", y)

#subconjunto(R, S)

# Dado dos conjuntos A y B, determina si A y B tienen al menos un elemento en común. Para hacer esto, puedes usar el método intersection() de 
# la clase set, y luego verificar si el conjunto resultante no está vacío.

def elementos_comun(A, B):
    comun = A.intersection(B)
    if len(comun) > 0:
        print(A, "y", B, "Tienen al menos un elemento en común")
    else:
        print(A, "y", B, "No tienen ningún elemento en común")
    
#elementos_comun(A, B)

# Crea una función en Python llamada eliminar_duplicados que tome una lista de números como argumento 
# y devuelva una nueva lista donde se hayan eliminado todos los elementos duplicados. Por ejemplo, si 
# la lista es [1, 2, 3, 1, 2, 3], la función debería devolver [1, 2, 3].

lista = [1, 2, 3, 1, 2, 3,4]
lista2 = [1, 2, 3, 1, 2, 3]

def eliminar_duplicados(lista):
    conjunto_nuevo = set(lista)
    list_resultado = list(conjunto_nuevo)
    print(list_resultado)

#eliminar_duplicados(lista)

# Crea una función en Python llamada intersección que tome dos listas de números como argumentos 
# y devuelva una nueva lista que contenga solo los elementos que estén presentes en ambas listas. 
# Por ejemplo, si las listas son [1, 2, 3] y [2, 3, 4], la función debería devolver [2, 3].

def intersección(lista, lista2):
    lista_comun = []
    l12 = set(lista).intersection(set(lista2))
    lista_comun.append(list(l12))
    print(lista_comun)

#intersección(lista, lista2)
#x_mas_y = set(lista) + set(lista2)
#print(x_mas_y)

# Crea una función en Python llamada diferencia que tome dos listas de números como argumentos 
# y devuelva una nueva lista que contenga solo los elementos que estén presentes en la primera lista, 
# pero no en la segunda. Por ejemplo, si las listas son [1, 2, 3] y [2, 3, 4], la función debería devolver [1].

def diferencia(x, y):
    lista_nueva = []
    differ_conj = set(x).symmetric_difference(set(y))
    lista_nueva.append(list(differ_conj))
    print (lista_nueva)

#diferencia(lista, lista2)


