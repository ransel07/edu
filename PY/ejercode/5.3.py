#5.3. Implementar una función que permita devolver un valor entero, leído desde teclado,
# comprendido entre dos límites que introduciremos como parámetro.


def valor_entero(x0, x1):

    z = int    

    if x0 < z < x1:
        print (z)
    else:
        print ("nope")

a = 50
b = 10

valor_entero(a,b)