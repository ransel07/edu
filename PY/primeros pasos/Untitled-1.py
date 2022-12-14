import math


#Valores a introducir
valor1= input("Valor #1 = ")
valor2= input("Valor #2 = ")

#Otros Valores
valor_super_random = 30
grados = 45
angulo1 = grados * 2 * math.pi / 360

Seno = math.sin(angulo1)
Coseno = math.cos(angulo1)
Tangente = math.tan(angulo1)

#print (Seno, Conseno, Tangente)

list = ["Maria", "Ronald", "Chistopher", "Sebastian", "Juan Jose", "Ransel", "Randel"]
lista2 = ["Juan", "Rodrigo"]


def nueva_funsion():
    print("Lista Numero 1:")

def nueva_funsion2():
    print("Lista Numero 2:")

def nueva_linea():
    print()

def dos_lineas():
    nueva_linea()
    nueva_linea()

def imprime_lista(argumento):       #Se les ha asignado argumento 
    print (argumento)               #Se ha colocado esos argumentos en el parametro

def imprime_matematicas(numero1):   #Se les ha asignado argumento 
    print (numero1)                 #Se ha colocado ese argumento en el parametro

def imprimejemplo(numero1):         #Se les ha asignado argumento 
    print (numero1, numero1)

#nueva_funsion()
#dos_lineas()
#imprime_lista(list)                 #Se sustitulle el argumento por la variable que se coloca 
#nueva_linea()
#imprime_matematicas(Seno*4)         #Se sustitulle el argumento por la variable que se coloca
#imprime_matematicas(Coseno*20)
#imprime_matematicas(Tangente*32)
#imprime_matematicas((grados))
#imprimejemplo(valor_super_random)
#nueva_linea()
#nueva_funsion2()
#dos_lineas()

#def revision_paridad(valor_super_random):
    
    if valor_super_random%2 == 0:
        print (valor_super_random, " Es par")

    else:
        print (valor_super_random, " Es impar")

def compara(valor1, valor2):
            
    if valor1 == valor2:
        
        print (valor1, "y", valor2, "son iguales")

    elif valor1 > valor2:
        
        print (valor1, "es mayor que", valor2)
    
    elif valor1 < valor2:
        print (valor1, "es menor que", valor2)

    else:
        print (valor1, "y", valor2, "son diferentes")
    return




compara(valor1, valor2)
#revision_paridad(grados)
