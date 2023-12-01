#5.9. Realizar una función que permita saber si una fecha es válida.

d = 29
h = 2

def fecha_valida(dia, mes):
    if 1 <= dia <= 31 and mes in [1, 3, 5, 7, 8, 10, 12]:
        print("Esta fecha es correcta")
    elif 1 <= dia <= 30 and mes in [4, 6, 9, 11]:
        print("Esta fecha es correcta")
    elif 1 <= dia <= 29 and mes == 2:
        print("Esta fecha es correcta")
    else:
        print("Esta fecha no es valida")

fecha_valida(d, h)