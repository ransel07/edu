
with open("estudiantes.txt", "r") as es:
    lineas = es.readline()
    mayor = max(es)
    contador = 0
    sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8 = 0, 0, 0, 0, 0, 0, 0, 0
    LineNew = []

    for elemento in lineas:
        LineNew.append(elemento)
    print(LineNew)
