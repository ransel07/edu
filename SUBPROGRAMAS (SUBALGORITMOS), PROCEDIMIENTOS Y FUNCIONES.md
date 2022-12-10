# SUBPROGRAMAS (SUBALGORITMOS), PROCEDIMIENTOS Y FUNCIONES

## La programación modular

La programación modular se refiere a la práctica de dividir un programa informático en módulos individuales que contienen código que realiza una tarea específica. Cada módulo se escribe de manera que pueda ser utilizado por otros módulos o programas, lo que hace que el desarrollo de software sea más eficiente y fácil de mantener.

La programación modular tiene varios beneficios, como la capacidad de reutilizar código, lo que reduce la cantidad de tiempo y esfuerzo necesarios para desarrollar un programa. También hace que el código sea más fácil de entender y mantener, ya que cada módulo se centra en una tarea específica y es más pequeño y manejable que un programa completo. Además, la programación modular también permite que varios programadores trabajen en diferentes módulos de un mismo programa al mismo tiempo, lo que facilita la colaboración en proyectos grandes y complejos.

## Declaracion de funciones

n programación, la declaración de funciones es la forma en que se define una función, es decir, un bloque de código que realiza una tarea específica y puede ser reutilizado en diferentes partes de un programa. Al declarar una función, especificas su nombre, qué argumentos o parámetros espera recibir y qué hace el código que contiene.

Por ejemplo, en Python, la declaración de una función puede tener la siguiente forma:

```.py
def my_function(x):
    # código que hace algo con el argumento x
```

En este ejemplo, se está declarando una función llamada my_function() que espera recibir un argumento llamado x. El código que se ejecuta cuando se llama a la función se encuentra indentado debajo de la línea de declaración, y puede hacer cualquier cosa con el argumento x, como, por ejemplo, multiplicarlo por 2:

```.py
def my_function(x):
    result = x * 2
    return result
```

Una vez que se ha declarado una función, puedes llamarla en cualquier parte del programa para ejecutar su código y obtener el resultado que deseas. Por ejemplo, si quieres llamar a la función my_function() y pasarle el argumento 5, puedes hacerlo de la siguiente manera:

Copy code
result = my_function(5)
Esto ejecutará el código de la función y asignará el resultado (en este caso, 10) a la variable result.

En resumen, la declaración de funciones es una herramienta importante en programación que te permite definir código que puede ser reutilizado en diferentes partes de un programa. Al declarar una función, especificas su nombre, qué argumentos espera recibir y qué hace el código que contiene, lo que te permite llamar a la función en diferentes partes del programa para ejecutar ese código y obtener el resultado que deseas.

## Declaracion de **Procedimientos**

La declaración de procedimientos en programación se refiere a la forma en que se define un procedimiento, que es un bloque de código que realiza una tarea específica, pero que no devuelve un valor al código que lo llamó. En lugar de devolver un valor, un procedimiento puede modificar variables o realizar otras acciones que afectan el estado del programa, pero no devuelve un resultado que pueda ser utilizado en otra parte del código.

Por ejemplo, supongamos que tienes una lista de números y quieres calcular el promedio de todos los números en la lista. En lugar de escribir el código que realiza el cálculo del promedio dentro del bucle que recorre la lista, puedes declarar un procedimiento llamado calculate_average() que contenga ese código:

```.py
def calculate_average(numbers):
    # código que calcula el promedio de los números en la lista
```

Luego, puedes llamar a ese procedimiento dentro del bucle que recorre la lista de números para calcular el promedio en cada iteración:

```.py
for number in numbers:
    average = calculate_average(number)
    # hacer algo con el promedio calculado
```

De esta manera, puedes separar el código que realiza el cálculo del promedio del código que controla la iteración sobre la lista, lo que hace que el programa sea más fácil de entender y mantener.

En resumen, la declaración de procedimientos se utiliza a menudo en programas que realizan tareas repetitivas, ya que permite separar el código que realiza la tarea de la lógica que controla la iteración sobre los datos, lo que hace que el programa sea más fácil de entender y mantener.

>>## Cuál es la diferencia entre Procedimientos y Funciones?
>>
>>La principal diferencia entre procedimientos y funciones es que las funciones devuelven un valor al código que las llamó, mientras que los procedimientos no lo hacen. En otras palabras, las funciones tienen una salida, mientras que los procedimientos no la tienen.
>>
>>La impresión de un mensaje en la pantalla se puede considerar una salida en el sentido de que el mensaje se muestra en la interfaz del programa y puede ser visto por el usuario. Sin embargo, en el contexto de la programación, la salida se refiere a un valor que se devuelve al código que llamó a una función o procedimiento.
>>
>>En el caso de un procedimiento como print_message(), que imprime un mensaje en la pantalla, no se devuelve ningún valor al código que lo llamó. Por lo tanto, se dice que el procedimiento no tiene una salida en el sentido de la programación.
>>
>>En cambio, en el caso de una función como area_circle(), que calcula el área de un círculo, se devuelve el resultado del cálculo al código que llamó a la función. En este caso, se dice que la función tiene una salida, ya que el resultado del cálculo puede ser utilizado en otra parte del programa.

## Paso de parametros

El paso de parámetros en programación se refiere a la forma en que se envían valores a una función o procedimiento cuando se llama a esta. Los parámetros son variables que se definen en la declaración de la función o procedimiento y que se utilizan para recibir los valores que se pasan como argumentos cuando se llama a la función o procedimiento.

Por ejemplo, supongamos que tienes una función que calcula el área de un círculo. La declaración de la función puede incluir un parámetro llamado radius, que se utilizará para recibir el radio del círculo cuando se llame a la función:

```.py
def area_circle(radius):
    # código que calcula el área del círculo
```

Cuando se llama a esta función, se puede pasar un argumento que especifique el radio del círculo para el cual se desea calcular el área. Por ejemplo, si quieres calcular el área de un círculo de radio 3, puedes llamar a la función de la siguiente manera:

```.py
area = area_circle(3)
```

En este ejemplo, el valor 3 se está pasando como argumento a la función area_circle(), y este valor se asigna al parámetro radius de la función. Luego, el código dentro de la función utiliza el valor de radius para calcular el área del círculo y devolver el resultado al código que llamó a la función.

>```.md
> Parametros formales e informales
>
>Los parámetros formales son aquellos que se utilizan en la definición de una función o procedimiento y que representan las variables que recibirán los valores que se envíen a la función o procedimiento. Por ejemplo, si una función tiene dos parámetros formales llamados x y y, entonces cuando se llame a esa función se deberán proporcionar dos argumentos que serán asignados a los parámetros formales x y y.
>
>Los parámetros actuales, por otro lado, son los argumentos que se envían a una función o procedimiento cuando se llama a esta. Por ejemplo, si se llama a la función mencionada anteriormente con dos argumentos 3 y 5, entonces los parámetros actuales serán 3 y 5 y estos valores serán asignados a los parámetros formales x y y dentro de la función.
>```

## Variables globales y locales

Las variables globales son aquellas que están disponibles en cualquier parte de un programa de computadora, incluyendo dentro de funciones y procedimientos. Esto significa que se pueden acceder y modificar desde cualquier lugar del programa. Las variables globales son útiles para almacenar y compartir información entre diferentes partes del programa.

Las variables locales, por otro lado, son aquellas que sólo están disponibles dentro de una función o procedimiento en el que han sido declaradas. Esto significa que no se pueden acceder ni modificar desde fuera de esa función o procedimiento. Las variables locales son útiles para almacenar y manipular información que sólo es relevante dentro de una función o procedimiento en particular.

La diferencia entre variables globales y locales es importante porque puede afectar el comportamiento de un programa. Las variables globales pueden ser modificadas desde cualquier lugar del programa, lo que puede causar conflictos si se modifican desde diferentes partes del programa. Las variables locales, por otro lado, sólo pueden ser modificadas dentro de la función o procedimiento en la que han sido declaradas, lo que evita conflictos y asegura que la información sólo sea manipulada de la manera esperada.
