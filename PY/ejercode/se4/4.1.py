#Ejercicio 4.1 Dado 3 numeros, deduzca cual es el central

num_1 = input("Introduzca el primer numero = ")
num_2 = input("Introduzca el segundo numero = ")
num_3 = input("Introduzca el tercer numero = ")

def numero_medio() :
    if num_1 > num_2 :
        if num_1 > num_3:
            print (num_3)
        
        elif num_2 > num_3:
            print(num_2)
        
        else:
            print(num_1)

numero_medio()