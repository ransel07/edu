#5.4. Diseñar una función que permita obtener el valor absoluto de un número.

print("ESCRIBE UN NUMERO PARA OBTENER SU VALOR ABSOLUTO")

num = int(input("Escribe el numero = "))  

def valor_abs(x):

    if x >= 0:
        print (x)
    else:
        nuevo_valor = x * -1
        print (nuevo_valor)
    

valor_abs(num)