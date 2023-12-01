# Crea una tupla con cinco elementos de cualquier tipo, luego imprímela en pantalla.

tupla = (1,2,3,4,5,2)
print(tupla)

# Crea una función que acepte una tupla como argumento y devuelva una lista con los mismos elementos de la tupla.

def convertidor_lista(tupla):
    print(list(tupla))

#convertidor_lista(tupla)

# Crea una función que acepte una tupla como argumento y devuelva un diccionario cuyas claves sean los 
# elementos de la tupla y cuyos valores sean el número de veces que cada elemento aparece en la tupla.

def colocar(tupla):
    diccionario = {}
    lista = list(tupla)
    for elemento in lista:
        valor = tupla.count(elemento)
        diccionario.update({valor : elemento})
    print(diccionario)
#colocar(tupla)

# Crea una función que acepte una tupla como argumento y devuelva una tupla con los elementos de la tupla original en orden inverso.

def inverso(tupla):
    print(tupla[::-1])

#inverso(tupla)

# Crea una función que acepte una tupla como argumento y devuelva una tupla con los elementos de la tupla original sin repeticiones.

def sin_repeticion(tupla):
    b = set(tupla)
    a = tuple(b)
    print(a)
#sin_repeticion(tupla)

# Crea una función que acepte una tupla como argumento y devuelva una tupla con los elementos de la tupla original ordenados de mayor a menor.

def mayor_menor(tp):
    j = sorted(tp, reverse=True)
    print(j)
    
mayor_menor(tupla)