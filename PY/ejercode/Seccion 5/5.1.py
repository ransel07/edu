#5.1. Realizar un procedimiento que permita intercambiar el valor de dos variables
variable1 = "Pepito"
variable2 = "Juanito"

def cambio_valor(x, y):
    aux = x
    x = y
    y = aux
    print(x, y)

cambio_valor(variable1, variable2)