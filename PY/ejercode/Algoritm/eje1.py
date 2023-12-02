'''
1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un 
muy buen ejercicio.
'''
def Maximo(a,b):
    if a>b :print (a)
    else: print (b)
# Maximo(5, 7)

'''
2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor 
de ellos.
'''
def max_de_tres(a,b,c):
    if a>b: 
        if a>c:print(a)
        else:print(c)
    else:
        if b>c:print(b)
        else:print(c)
# max_de_tres(5,7,3)

def max_de_tres(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
'''
5 - Escribir una función sum() y una función multip() que sumen y multipliquen 
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) 
debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
'''
def suma(args):
    n=0
    for num in args:
        n=n+num
    return n

# print (suma([1,2,3,4,5]))

# def multplicacion(lista):


''' 
Escribe una función que tome un número entero positivo como entrada y devuelva
la suma de todos los números pares menores o iguales a ese número.
'''

def funsion(num):
    if num % 2 == 0 and num > 0:
        box=0
        for n in range(num+1):
            box= box + n
        print (box)
    else:
        print ('Este numero no es par, o, es negativo')

# funsion(10)

'''
Escribe una función que tome una cadena de texto como entrada y devuelva su inversa. 
Por ejemplo, si la cadena de entrada es "Hola", la salida debería ser "aloH".
'''
def inversa_cadena(cadena):
    num = len(cadena) - 1
    lista = []
    for i in cadena:
        lista.append(cadena[num])
        num=num-1
    cadena2=''
    for e in lista:
        cadena2 = cadena2 + e
    print (cadena2)
# inversa_cadena('Presidente')

'''
Escribe una función que tome un número entero positivo como entrada y determine si es un 
número de Armstrong o no. Un número de Armstrong es aquel número que es igual a la suma de 
sus dígitos elevados a la potencia del número de dígitos.
'''

def numero_Armstrong(num):
    a=str(num)
    return a[1]

print (numero_Armstrong(153))


















