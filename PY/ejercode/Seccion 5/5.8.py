#5.8. Diseñar una función que permita obtener el máximo común divisor de dos números mediante el algoritmo de Euclides.



def MCD(num1, num2):
    #algoritmo de Euclides
    if num1 > num2:
        resto = num1 % num2
    