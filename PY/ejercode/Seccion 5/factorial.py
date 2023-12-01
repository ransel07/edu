#Diseñe una función que permita obtener el factorial de un número entero positivo.

import math

x = int(input())

def factorial(num_entero):

    if  num_entero > 0:
        print (math.factorial(num_entero))
    else:
        print("No es un nuemro positivo")

factorial(x)