# **PROGRAMACIÓN ESTRUCTURADA**

La programación estructurada es un paradigma de programación que se basa en la estructuración de un programa en bloques de código independientes que se ejecutan secuencialmente. La programación estructurada se enfoca en la organización y la estructura del código, y tiene como objetivo hacer que los programas sean más fáciles de leer, entender y mantener.

## **TEOREMA DE BÖHM Y JACOPINI**

El teorema de Böhm y Jacopini es un teorema en teoría de la computación que establece que todo algoritmo computable puede ser escrito como una secuencia de bloques de código que utilizan solo tres estructuras de control de flujo: <span style = "color:red">**secuencia, selección y iteración**</span>. 

El teorema fue propuesto por el matemático alemán Corrado Böhm y el informático italiano Giuseppe Jacopini en 1966, y demostró que cualquier algoritmo que pueda ser escrito utilizando estructuras de control de flujo más complejas, como el case o el switch, también puede ser escrito utilizando solo las tres estructuras básicas mencionadas. Esto demuestra que las estructuras de control de flujo más complejas no son necesarias para realizar cualquier tipo de tarea computable, y que la programación estructurada puede ser utilizada para escribir cualquier algoritmo computable de manera clara y eficiente.

En resumen, esto demuestra la eficiencia y flexibilidad de la programación estructurada para escribir algoritmos computables de manera clara y eficiente.

## **Control de flujo**

Que tiene que ver la programación estructurada con el control de flujo?

El control de flujo es una herramienta utilizada en la programación estructurada para _**modificar el flujo de ejecución de un programa**_. El control de flujo permite a un programa tomar decisiones y ejecutar diferentes bloques de código en función de ciertas condiciones o situaciones. Esto permite a un programa adaptarse a diferentes entradas o situaciones y resolver problemas de forma más eficiente y flexible.

En resumen, la programación estructurada y el control de flujo están relacionados porque el control de flujo es una herramienta utilizada en la programación estructurada para modificar el flujo de ejecución de un programa y adaptarlo a diferentes situaciones.

Las sentencias de <span style="color:red"> selección </span>. son: si («if») y según-sea («switch»); las sentencias de <span style="color:yellow">repetición o iterativas</span> son: desde («for»), mientras («while»), hacer-mientras («do-while») o repetir-hasta que («repeat-until»); las sentencias de <span style="color:green">salto</span> incluyen interrumpir (break), continuar (continue), ir-a (goto), volver (return) y lanzar (trhow).

>### **Estructura Secuencial**

La estructura secuencial es una estructura de control de flujo que se utiliza para ejecutar una secuencia de bloques de código de manera secuencial, es decir, uno después del otro. La estructura secuencial es la estructura de control de flujo más básica y se utiliza para ejecutar un conjunto de instrucciones en el orden en que aparecen en el código.

>### **Estructura selectiva (condicionales)**

Una estructura selectiva es aquella en que se ejecutan unas acciones u otras según se cumpla o no una
determinada condición. La selección puede ser simple, doble o múltiple.

>### **Estructura repetitiva (bucle)**

Una estructura repetitiva es un tipo de estructura de control en un programa de computadora que se utiliza para ejecutar un bloque de código varias veces de manera repetida. La idea es que el código se ejecute en un bucle, repitiéndose hasta que se cumpla una cierta condición. Hay varios tipos diferentes de estructuras repetitivas, como el bucle for y el bucle while. En ambos casos, se especifica una condición que se utiliza para determinar cuándo se detiene el bucle y se continúa con la ejecución del código después del bucle.

Un centinela es un valor especial que se utiliza en una estructura repetitiva para determinar cuándo se debe detener el bucle. Por ejemplo, si estamos recorriendo una lista de números y queremos detener el bucle cuando lleguemos a un cierto valor, podemos utilizar un centinela como ese valor especial. Cuando el bucle encuentra el centinela, detiene la ejecución y continúa con el código después del bucle. Esto es útil porque nos permite controlar exactamente cuándo se detiene el bucle y evitar que se ejecute de manera infinita.

```py
# Esta es una lista de números enteros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# El centinela es el número 6
centinela = 6

# Recorremos la lista de números
for numero in numeros:
  # Si encontramos el centinela, detenemos el bucle
  if numero == centinela:
    break
  # Si el número no es el centinela, lo imprimimos en pantalla
  print(numero)

# Este mensaje se imprimirá después del bucle
print("Fin del bucle")
```

### **Estructura de salto**

La estructura de salto, que permite que un programa salte a una línea específica de código. Las estructuras de salto incluyen las sentencias break, continue y goto.

### **Estructura de anidada**

La estructura anidada se refiere a la forma en que se incluyen unas estructuras de control de flujo dentro de otras. Por ejemplo, una sentencia if puede estar anidada dentro de una sentencia for, lo que significa que la sentencia if se ejecutará cada vez que se itere el ciclo for. De esta manera, se pueden crear estructuras de control de flujo más complejas y adaptables a diferentes situaciones.

Tanto las estructuras selectivas como las repetitivas pueden ser anidadas, e introducidas unas en el interior
de otras.
