#Realizar un algoritmo que averigüe si dados dos números introducidos por teclado,
#uno es divisor del otro.

a = int(input())
b = int(input())

if a % b == 0:
    print (a, "es divisor de ", b)
elif b % a == 0:
    print (b, "es divisor de ", a)
else:
    print ("Ninguno es devisor del otro")
