#5.6. Diseñar un procedimiento que permita convertir coordenadas polares (radio, ángulo)
# en cartesianas (x,y)
# x = radio * cos(ángulo)
# y = radio* sen(ángulo)

import math

def convertidor_cartesianas(radio, ángulo):
    x = radio * math.cos(ángulo)
    y = radio* math.sen(ángulo)
    print(x, y)