def f():
    def intercambion(lista):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

    lista = [5, 2, 8, 1, 4]
    intercambion(lista)
    print(lista)


def quicksort(lista):
    
    if len(lista) < 2:
        return lista
    
    pivote = lista[(len(lista) - 1)//2]

    left = []
    for num in lista:
        if num <= pivote:
            left.append(num)
    
    right = []
    for num in lista:
        if num > pivote:
            right.append(num)
    
    

    return quicksort(left) + [pivote] + quicksort(left)
lista = [5, 2, 8, 1, 4]
oredemado = quicksort(lista)
print (oredemado)
