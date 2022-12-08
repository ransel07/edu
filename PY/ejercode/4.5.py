#dia = int(input("Introduzca el día = "))
#mes = int(input("Introduzca el Mes = "))
#año = int(input("Introduzca el Año = "))

# Diseñar un algoritmo en el que a partir de una fecha introducida por teclado con el formato DÍA,
# MES, AÑO, se obtenga la fecha del día siguiente.

def dia_despues():
    dia = int(input("Introduzca el día = "))
    mes = int(input("Introduzca el Mes = "))
    año = int(input("Introduzca el Año = "))

    if dia == 29 or 28 and mes == 2:
        dia = dia - 28 or dia - 27
        mes = mes + 1
        print("Día ", dia, "Mes ", mes, "Año ", año)

    elif dia == 30:
        dia = dia - 29
        mes = mes + 1
        año = año + 1
        print("Día ", dia, "Mes ", mes, "Año ", año)

    elif dia == 31 and mes == 12:
        
        dia = dia - 30
        mes = mes - 11
        año = año - 1
        print("Día ", dia, "Mes ", mes, "Año ", año)

    else:
        dia = dia - 30
        mes = mes + 1
        año = año + 1
        print("Día ", dia, "Mes ", mes, "Año ", año)


dia_despues()