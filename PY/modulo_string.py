frase_de_vida = "Miedo es la palabra a la que nos aferramos para no intentar lo posible"
indice = frase_de_vida.find("aferramos")


def nueva_linea():
    print()

nueva_linea()
print("Subindice donde 'aferramos' se encuentra en el grupo de caracteres:", indice)

import string

# Constantes de módulo string (cadenas)
print(string.ascii_letters)    #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  #abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  #ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)           #0123456789
print(string.hexdigits)        #0123456789#abcdefABCDEF
print(string.whitespace)  # ' \t\n\r\x0b\x0c' - Dos especios
print(string.punctuation) # !"#$%&'()*+,-./:;?@[\]^_`{|}~ Signos de puntuación 