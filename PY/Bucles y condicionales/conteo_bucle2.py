print("DETERMINE LA CANTIDAD DE LETRAS, O, I Y P QUE TIENRE SU TEXTO ")
cadena = input("Digite su texto: ")


def contar_letras(cadena):
    contador = 0   #
    contador2 = 0
    contador3 = 0

    for elemento in cadena:  #Para cada variable (elemento) que toma el valor del...
    #...elemento dentro del iterador en la variable "cadena"

        if elemento == "o":  #la condición seria que, si el elemento es 'o'...
    #...la siguiente fase seria aumentar el contador sumandole 1.
            contador = contador + 1

        elif elemento == "i": #la condición seria que, si el elemento es 'i'...
    #...la siguiente fase seria aumentar el contador sumandole 1.
            contador2 = contador2 + 1 

        elif elemento == "p":
            contador3 = contador3 + 1
    print("La frase:")
    print(cadena)
    print("Tiene", contador, "letras o")
    print("Tiene", contador2, "letras i")
    print("Tiene", contador3, "letras p")


contar_letras(cadena)

#Serie bueno pensar en una forma para hacer el conteo de todas y cada una de las letras y especificar 
#cuantas hay de cada una.