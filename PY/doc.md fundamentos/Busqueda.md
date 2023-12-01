# ORDENACIÓN, BÚSQUEDA E INTERCALACIÓN INTERNA

## Busqueda

La búsqueda es una de las operaciones más importantes en el procesamiento de la información, y permite la recuperación de datos previamente almacenados. Cuando el almacenamiento se encuentra en memoria principal la búsqueda se califica de interna. En este capítulo se consideran los datos almacenados en arrays y se analiza el modo de realizar operaciones de ordenación, fusión o búsqueda en ellos.

## Métodos de búsqueda más comunes

**Búsqueda secuencial**: es un método de búsqueda simple en el que se examina cada elemento de la lista secuencialmente hasta encontrar el elemento buscado o determinar que el elemento no está en la lista.

**Búsqueda binaria**: es un método de búsqueda más eficiente que la búsqueda secuencial. En este método, se divide la lista en dos mitades y se elige la mitad que contiene el elemento buscado. Luego se continúa la búsqueda en esa mitad de la lista.

**Búsqueda hashing**: es un método de búsqueda que utiliza una función de hash para mapear cada elemento de la lista a un índice de una tabla hash. Esto permite acceder directamente al elemento buscado en la tabla hash sin tener que recorrer la lista completa.

**Búsqueda árbol**: es un método de búsqueda que utiliza un árbol para almacenar y organizar los elementos de la lista. La búsqueda se realiza comparando el elemento buscado con el elemento en la raíz del árbol y eligiendo el subárbol apropiado para continuar la búsqueda.

**Búsqueda gráfica**: es un método de búsqueda que utiliza un grafo para representar y almacenar los elementos de la lista. La búsqueda se realiza siguiendo las relaciones entre los nodos del grafo hasta encontrar el elemento buscado.

### Busqueda binaria

La búsqueda binaria es un algoritmo de búsqueda que se utiliza para encontrar un elemento en una lista ordenada. La idea principal detrás de la búsqueda binaria es dividir repetidamente la lista en dos partes hasta que el elemento sea encontrado.

```.py

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
lista = [1, 2, 3, 4, 5]
indice = binary_search(lista, 3)
if indice == -1:
    print("El elemento no se encuentra en la lista")
else:
    print("El elemento se encuentra en el índice", indice)


```

- Ejemplo 2:

```.py

def busqueda_binaria(lista, elemento):
    límite_inferior = 0
    límite_superior = len(lista) - 1
    while límite_inferior <= límite_superior:
        índice_medio = (límite_inferior + límite_superior) // 2
        if lista[índice_medio] == elemento:
            return índice_medio  # Se ha encontrado el elemento, se devuelve el índice
        elif lista[índice_medio] < elemento:
            límite_inferior = índice_medio + 1  # El elemento buscado es mayor, se actualiza el límite inferior
        else:
            límite_superior = índice_medio - 1  # El elemento buscado es menor, se actualiza el límite superior
    return -1  # Se ha llegado al final de la lista sin encontrar el elemento, se devuelve -1

# Prueba la función busqueda_binaria
lista = [1, 3, 4, 6, 7, 8, 9, 10]
print(busqueda_binaria(lista, 6))  # Imprime 3
print(busqueda_binaria(lista, 5))  # Imprime -1

```
