# **ESTRUCTURAS DE DATOS (ARRAYS Y REGISTROS)**

## Indice

* [Conjuntos](#conjuntos)
  * [Implementación](#implementación)
* [Diferencias entre conjuntos y listas en Python](#además-de-lo-mencionado-anteriormente-hay-varias-diferencias-importantes-entre-conjuntos-y-listas-en-python)

## ***Conjuntos***

Un conjunto (set en inglés) es un tipo de dato en Python que se usa para almacenar una colección de elementos sin ningún orden en particular y sin elementos duplicados. Los conjuntos son muy útiles cuando queremos realizar operaciones matemáticas como la unión, intersección y diferencia de conjuntos.

Para crear un conjunto en Python, puedes usar la función set() o simplemente usar llaves {}. Por ejemplo:

```.py
# Crea un conjunto vacío
empty_set = set()

# Crea un conjunto con elementos
numbers = {1, 2, 3, 4, 5}

# Crea un conjunto a partir de una lista
numbers_list = [1, 2, 3, 4, 5]
numbers_set = set(numbers_list)
```

Los conjuntos son muy útiles cuando queremos eliminar elementos duplicados de una colección de datos. Por ejemplo, si tenemos una lista de números y queremos eliminar los duplicados, podemos convertir la lista en un conjunto y luego volver a convertirla en una lista.

Para convertir una lista en un conjunto, puede utilizar la función built-in set() de Python. Por ejemplo:

```.py
mi_lista = [1, 2, 3, 1, 2, 3]
mi_conjunto = set(mi_lista)

print(mi_conjunto)  # imprime: {1, 2, 3}
```

Para convertir un conjunto en una lista, puede utilizar la función built-in list() de Python. Por ejemplo:

```.py
mi_conjunto = {1, 2, 3}
mi_lista = list(mi_conjunto)

print(mi_lista)  # imprime: [1, 2, 3]
```

Es importante tener en cuenta que, al convertir un conjunto en una lista, el orden de los elementos en la lista resultante no estará garantizado.

### Además de lo mencionado anteriormente, hay varias **diferencias importantes entre conjuntos y listas en Python**
>
>* Los conjuntos no tienen un orden fijo, lo que significa que no se pueden acceder a sus elementos mediante un índice. En cambio, las listas sí tienen un orden fijo, por lo que se pueden acceder a sus elementos mediante un índice.
>
>* Los conjuntos no admiten elementos duplicados, mientras que las listas sí pueden contener elementos duplicados.
>
>* Los conjuntos son más rápidos que las listas cuando se realizan operaciones de búsqueda y pertenencia. Esto se debe a que los conjuntos utilizan una implementación interna llamada "tabla hash", que permite realizar estas operaciones en tiempo constante en promedio. En cambio, las listas utilizan una implementación basada en arreglos, lo que requiere recorrer la lista completa para realizar operaciones de búsqueda y pertenencia.
>
>* Los conjuntos ofrecen una serie de operaciones matemáticas que no están disponibles para las listas, como la unión, intersección y diferencia de conjuntos. Estas operaciones se pueden realizar utilizando operadores o funciones específicas de conjuntos, como union(), intersection() y difference().

### Implementación

En términos de implementación, las listas y los conjuntos pueden implementarse de diferentes maneras en función del lenguaje de programación que se esté utilizando. Por ejemplo, en algunos lenguajes de programación, las listas se implementan como arreglos, mientras que los conjuntos se implementan como tablas de hash.

En términos de ventajas y desventajas, las listas tienen la ventaja de que permiten el acceso aleatorio a los elementos mediante un índice, lo que las hace ideales para realizar operaciones como buscar, ordenar o insertar elementos en una posición específica. Sin embargo, esta ventaja también puede ser una desventaja, ya que el acceso aleatorio a los elementos puede ser lento si la lista es muy larga.

Las listas en Python se implementan usando arrays dinámicos, lo que significa que pueden crecer y reducirse dinámicamente en tamaño para adaptarse a los cambios en el número de elementos que contienen. Esto hace que las listas sean muy versátiles y fáciles de usar, pero también puede hacerlas menos eficientes en términos de tiempo y espacio en comparación con otras estructuras de datos.

Los conjuntos en Python se implementan usando tablas de hash, lo que les permite realizar operaciones de búsqueda y actualización en tiempo constante en promedio. Esto los hace muy eficientes en términos de tiempo y espacio, pero requieren que los elementos que se almacenan en ellos sean hashables, lo que significa que deben tener una función de hash definida.

## tablar hash

Las tablas de hash son estructuras de datos que se utilizan para almacenar y recuperar información de manera rápida. Estas tablas asocian una "clave" con un "valor" y utilizan una función llamada "función hash" para calcular dónde se debe almacenar cada clave en la tabla. Esto permite que se pueda acceder a cualquier valor de la tabla de manera eficiente, simplemente proporcionando su clave. Las tablas de hash son utilizadas en muchos campos, como la informática, la criptografía y la estadística, para hacer que el acceso y la búsqueda de datos sea más rápido y eficiente.

Una función hash es una función matemática que toma una entrada de cualquier tamaño y la convierte en una salida de tamaño fijo. Esta salida se conoce como "valor hash" o "valor resumen". Las funciones hash se utilizan en muchas aplicaciones diferentes, como la criptografía, la verificación de la integridad de los datos, y las tablas de hash. Una función hash es una función que es rápida de calcular y que produce un valor único para cada entrada. Esto permite que se puedan comparar rápidamente dos entradas para ver si son iguales, simplemente comparando sus valores hash. También se utilizan en las tablas de hash para determinar dónde se almacena una determinada clave en la tabla.

Ejemplo sencillo de una función hash:

```.py
def hash_function(key):
  # convierte la clave en un entero
  key_int = int(key)
  # aplica una operación matemática a la clave
  # para producir un valor hash
  hash_value = key_int % 10
  return hash_value

# usa la función hash para calcular dónde se almacena una clave
key1 = "foo"
key2 = "bar"
key3 = "baz"

hash1 = hash_function(key1)
hash2 = hash_function(key2)
hash3 = hash_function(key3)

print(hash1) # imprime 3
print(hash2) # imprime 4
print(hash3) # imprime 9

```

En este ejemplo, la función hash toma una clave como entrada y la convierte en un entero. Luego, aplica una operación matemática simple (el módulo 10) para producir un valor hash. Este valor hash se utiliza para determinar dónde se almacena la clave en la tabla de hash.
