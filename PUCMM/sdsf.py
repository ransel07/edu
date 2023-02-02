teclado = input("inserte = ")
lista = []
def element_count(teclado, lista):
    while teclado != "q":
        if teclado in lista:
            teclado = input("inserte = ")
        else:
            lista.append(teclado)
            teclado = input("inserte = ")
    record = {}
    for element in lista:
        n = lista.count(element)
        record[element] = n
    print (record)


element_count(teclado, lista)

