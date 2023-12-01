n = int(input ("# = "))

def cuenta_atras(n):
    if n == 0:
        print("Despegamos")
    else:
        print(n)
        cuenta_atras(n-1)
    

cuenta_atras(n)