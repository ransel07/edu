import math

##radio = int(input("Radio = "))
x = int(input("x = "))
y = int(input("y = "))

def area(radio):
    
    print (math.pi * radio**2)

#area(radio)

def comparar2():
    if x > y:
        print(1)
    elif x == y:
        print(0)
    