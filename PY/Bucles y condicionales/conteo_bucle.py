
cadena = "Miedo es la palabra a la que nos aferramos para no intentar lo posible"
contador = 0

for elemento in cadena:  #Para cada variable (elemento) que toma el valor del...
#...elemento dentro del iterador en la variable "cadena"

    if elemento == "o":         #la condición seria que, si el elemento es 'o'...
#...la siguiente fase seria aumentar el contador sumandole 1.
        contador = contador + 1

print (contador)
