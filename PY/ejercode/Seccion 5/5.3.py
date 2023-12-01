#5.3. Implementar una función que permita devolver un valor entero, leído desde teclado,
# comprendido entre dos límites que introduciremos como parámetro.

a = 0
b = 10000000

def valor_entero(x0, x1):
    
    print("ESCRIBE UN NUMERO QUE ESTE ENTRE", x0, "y", x1)
    
    z = int(input("Escribe el numero = "))    

    if x0 <= z <= x1:
        print (z, "Si esta entre", x0, "y", x1)
    else:
        print (z, "No esta entre", x0, "y", x1)
    valor_entero(x0, x1)

valor_entero(a,b)

