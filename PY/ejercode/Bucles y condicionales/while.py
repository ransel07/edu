#Como activida, reescriba la función nLines de la sicción 4.9 utilizando 
# iteracción en lugar de recursividad

print("INTRODUCE DESDE DONDE EMPIEZA EL CONTEO")

def lineaen_blanco():
    print()

lineaen_blanco()

n = int(input("Desde que numero empezar = "))

lineaen_blanco()

def cuenta_atras(n):
    while n > 0:
        print(n)
        n=n-1
    print("Despeguemos!")
        

cuenta_atras(n)



