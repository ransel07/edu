#5.10. Implementar una función que permita hallar el valor de Xy, siendo X un número real e y un entero.

e = 2
e2 = 2

import math

def calcular_valor_xy(x: float, y: int) -> float:
    return print (math.pow(x, y))                         #Puede ser "return x ** y" & "return math.pow(x, y)"

calcular_valor_xy(e, e2)