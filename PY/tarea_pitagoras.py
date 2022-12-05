#como actividad utilice el desarrollo incremental para escribir una función de nombre [hipotenusa] 
#que devuelva la logitud de la longitud de la hipotenusa de un triangulo rectangulo, dado como parametro
# los dos catetos. registe cada estado del desarrollo icremental seun vaya avanzando
import math

print("PROGRAMA PARA CALCULAR PROBLEMA BASICO DE PITAGORAS SOLO INTRODUZCA X & Y")

def nueva_linea():
    print()

def dos_lineas():
    nueva_linea()
    nueva_linea()

nueva_linea()
x = int(input("Base (X) = "))
y = int(input("Altura (Y) = "))


def hipotenusa(x, y):
    equi_a_la_do = x**2                                                         #Cuadrado de x 
    ye_a_la_do = y**2                                                           #Cuadrado de y
    suma_de_los_cuadraros = equi_a_la_do + ye_a_la_do                           #Suma de los cuadrados
    nueva_linea()
    print("EL RESULTADO DE ", x, "y", y, "ES: ",math.sqrt(suma_de_los_cuadraros))#se improme la Raiz cuadrada de
    return 0.0
 

hipotenusa(x, y)
