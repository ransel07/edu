#5.5. Realizar un procedimiento que obtenga la división entera y el resto de la misma utilizando
# únicamente los operadores suma y resta.

a = 14
b = 3

def cociente_resto(numerador, denominador):
    contador = 0                                   #contador para tener el numero de veces que se ejecuta un ciclo
    denominador_cociente = 0                      # "denominador_cociente" 
    cociente = numerador / denominador 

    while cociente >= contador:

        contador = contador + 1

        denominador_cociente = denominador_cociente + denominador  #sumar "cociente" veces el "denominador"

        if contador == cociente:
            resto = numerador - denominador_cociente
            print (cociente, resto)


# Si hago lo que dices de sustiturir "contador" con "denominador_cociente" el ciclo acabara antes de que "denominador_cociente" se sume "cociente" veces. Entonces cuando se ejecute el segundo ciclo, se procedera a realizar el calculo de la variable "resto"

cociente_resto(a, b)



#repetir 

#j = 10/2
#i = 10 % 2
#k = 10 - j*2 

#print(j)
#print(k)
#print(i)