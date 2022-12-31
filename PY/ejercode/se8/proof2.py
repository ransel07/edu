"______________________________________________________________________"
"Crea una función llamada busqueda_binaria_recursiva que haga lo mismo"
"que la función anterior, pero de forma recursiva."
"______________________________________________________________________"


def busqueda_binaria_recursiva(lista, num, left, right, count):
    if left > right :
        return f"no se ha entontrado {num} en la lista"
    middle = (left + right) // 2
    count += 1
    if lista[middle] == num:
        return f"El numero {num} si esta en la lista; Numero de intentosintentos: {count}"
    elif lista[middle] < num:
        return busqueda_binaria_recursiva(lista, num, middle + 1, right, count)
    else:
        return busqueda_binaria_recursiva(lista, num, left, middle - 1, count)

switch = True
while switch:
    lista = []
    for numb in range(21):
        lista.append(numb)
    num = int(input("numero a buscar = "))
    if num == -99:
        switch = False
    else:
        p = busqueda_binaria_recursiva(lista, num, 0, len(lista), 0)
        print(p)
