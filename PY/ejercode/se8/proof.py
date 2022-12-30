empleados = [{"nombre": "Juan", "edad": 25, "salario": 1500, "puesto": "Programador", "tiempo_trabajando": 2},
{"nombre": "Ana", "edad": 30, "salario": 2000, "puesto": "Analista de datos", "tiempo_trabajando": 5},
{"nombre": "Pedro", "edad": 35, "salario": 2500, "puesto": "Jefe de proyecto", "tiempo_trabajando": 10},
{"nombre": "Sofía", "edad": 40, "salario": 3000, "puesto": "Gerente de TI", "tiempo_trabajando": 15},
{"nombre": "Mario", "edad": 45, "salario": 3500, "puesto": "Director de TI", "tiempo_trabajando": 20}]

def binary_search(lista, elemento):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif elemento < lista[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return -1

# Ejemplo de uso
lista = [range(1,10)]
indice = binary_search(lista, 3)
if indice == -1:
    print("El elemento no se encuentra en la lista")
else:
    print("El elemento se encuentra en el índice", indice)


# Crea una función llamada "busqueda_binaria" que reciba como parámetros un arreglo de números enteros 
# ordenados y un número a buscar. La función debe devolver la posición del número en el arreglo, o -1 
# si no se encuentra.

def search_binary(lista, num):
    left_numb = 0
    right_numb= len(lista)
    if num == left_numb:
        return lista[num]
    if num == right_numb:
        return
    else:
        left_numb += 1
        right_numb -= 1