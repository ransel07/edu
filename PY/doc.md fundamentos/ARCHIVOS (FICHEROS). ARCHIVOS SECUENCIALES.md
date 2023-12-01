# **ARCHIVOS (FICHEROS). ARCHIVOS SECUENCIALES**

* [Archivos](#archivos)
* [Jerarquización](#jerarquización)
* [Flujos](#flujos)

## Archivos

Los archivos de programas son archivos que contienen código fuente o código ejecutable de un programa informático. Los archivos de datos, por otro lado, son archivos que contienen información que puede ser utilizada por un programa informático.

### Archivos de programas y de datos

Los archivos de programas pueden ser de diversos tipos, como archivos de código fuente escritos en un lenguaje de programación, archivos ejecutables que contienen código ya compilado y listo para ser ejecutado por la máquina, archivos de bibliotecas o librerías que contienen código que puede ser utilizado por otros programas, y otros tipos de archivos relacionados con la ejecución de programas.

Los archivos de datos, por otro lado, pueden ser de diversos tipos, como archivos de texto que contienen información en forma de texto legible por un ser humano, archivos de imágenes que contienen información en forma de imágenes, archivos de audio que contienen información en forma de audio, y otros tipos de archivos que contienen información en diferentes formatos.

Los archivos de programas y de datos son esenciales en la informática, ya que permiten almacenar y utilizar la información necesaria para la ejecución de programas y la realización de tareas específicas.
El registro físico de un archivo es la posición física del archivo en el disco duro o en otro dispositivo de almacenamiento. Esta posición se determina por la ubicación de los sectores de datos en el dispositivo de almacenamiento en los que se guarda el archivo.

### registro físico y logico

El registro lógico, por otro lado, es la representación del archivo en el sistema de archivos. El sistema de archivos es una estructura de datos que se utiliza para organizar y almacenar archivos en un dispositivo de almacenamiento. El registro lógico incluye información como el nombre del archivo, el tamaño del archivo, la fecha de creación y modificación del archivo, y otros atributos del archivo.

El registro físico y el registro lógico son dos conceptos diferentes, pero están relacionados ya que el registro lógico se utiliza para hacer referencia al registro físico del archivo. Por ejemplo, cuando se accede a un archivo a través del sistema de archivos, se utiliza el registro lógico para determinar la posición física del archivo en el disco duro y leer los datos del archivo.

### Facto de bloqueo

El factor de bloqueo en archivos se refiere a la cantidad de espacio en el disco duro o en otro dispositivo de almacenamiento que se asigna a un archivo cada vez que se escribe en él. El factor de bloqueo se utiliza para optimizar el rendimiento del sistema de archivos y para reducir el número de operaciones de lectura y escritura necesarias para acceder y manipular los archivos.

Cuando se escribe un archivo en un disco duro o en otro dispositivo de almacenamiento, el sistema de archivos divide el archivo en una serie de bloques de datos de tamaño fijo, conocidos como bloques de disco. El factor de bloqueo se refiere al tamaño de cada uno de estos bloques de disco. Si el factor de bloqueo es grande, cada bloque de disco tendrá más espacio y se podrán almacenar más datos en cada uno, lo que puede reducir el número de operaciones de lectura y escritura necesarias para acceder y manipular el archivo. Sin embargo, si el factor de bloqueo es pequeño, habrá más bloques de disco necesarios para almacenar el archivo y se necesitarán más operaciones de lectura y escritura para acceder y manipular el archivo.

Imagina que tenemos un archivo de texto de 500 KB que queremos almacenar en un disco duro. Si el factor de bloqueo del disco duro es de 4 KB, el sistema de archivos dividirá el archivo en 125 bloques de disco de 4 KB cada uno. Esto significa que se necesitarán 125 operaciones de lectura y escritura para acceder y manipular el archivo completo.

### Archivos en Python

En Python, los archivos (también conocidos como ficheros) son una forma de almacenar información en disco. Se pueden usar archivos para leer y escribir datos en diferentes formatos, como texto, CSV (valores separados por coma) o JSON (un formato de intercambio de datos basado en texto).

Para trabajar con archivos en Python, primero debemos abrirlos utilizando la función open(). Esta función toma dos argumentos: el nombre del archivo y el modo en que se abrirá el archivo. Los modos más comunes son "r" (lectura), "w" (escritura) y "a" (agregar).

Por ejemplo, para abrir un archivo de texto llamado "mi_archivo.txt" en modo lectura, podemos utilizar el siguiente código:

```.py
with open("mi_archivo.txt", "r") as archivo:
  # Código para trabajar con el archivo
  ```

La palabra clave with se utiliza para asegurar que el archivo se cierre correctamente una vez que hayamos terminado de trabajar con él. El archivo se asigna a la variable archivo, que podemos utilizar para leer el contenido del archivo.

Para leer el contenido de un archivo, podemos utilizar el método `read()` de la variable archivo. Este método devuelve todo el contenido del archivo como una cadena de texto.

```.py
with open("mi_archivo.txt", "r") as archivo:
  contenido = archivo.read()
  print(contenido)
  ```

Para escribir en un archivo, podemos utilizar el método `write()` de la variable archivo. Este método toma una cadena de texto como argumento y escribe esa cadena en el archivo.

```.py
with open("mi_archivo.txt", "w") as archivo:
  archivo.write("Hola, mundo!")
  ```

Para agregar texto al final de un archivo existente, podemos utilizar el modo "a" en lugar de "w":

```.py
with open("mi_archivo.txt", "a") as archivo:
  archivo.write("\nAdiós, mundo!")
  ```

Es importante tener en cuenta que el modo "w" sobrescribe el contenido del archivo, mientras que el modo "a" agrega texto al final del archivo sin sobrescribir lo que ya existe.

## Jerarquización

La jerarquización de los datos es el proceso de organizar y estructurar los datos de manera que sean fáciles de acceder y utilizar. La jerarquización de los datos puede hacerse de varias maneras, dependiendo del tipo y la cantidad de datos que se tengan, así como del propósito para el cual se vayan a utilizar.

Una forma común de jerarquizar los datos es mediante la utilización de estructuras de datos jerárquicas, que consisten en una serie de elementos que están organizados en una jerarquía de niveles. Por ejemplo, en un sistema de archivos, los archivos y las carpetas se organizan en una jerarquía de niveles en la que cada carpeta puede contener otros archivos y carpetas.

Otra forma de jerarquizar los datos es mediante la utilización de bases de datos relacionales, que consisten en un conjunto de tablas de datos relacionadas entre sí mediante claves foráneas. Las bases de datos relacionales permiten la jerarquización de los datos mediante la creación de relaciones entre tablas de datos y la utilización de consultas para acceder y manipular los datos de manera eficiente.

### Operaciones básicas

En Python, puedes realizar varias operaciones básicas con archivos utilizando la función open() y los métodos de archivo. Algunas de las operaciones básicas que puedes realizar son:

* Abrir un archivo: para abrir un archivo en Python, puedes usar la función open(). Esta función toma dos argumentos: el nombre del archivo y el modo en el que quieres abrirlo. Los modos más comunes son "r" para leer, "w" para escribir y "a" para agregar contenido al final del archivo. Por ejemplo:

```.py
f = open("myfile.txt", "r")
```

* Leer un archivo: una vez que has abierto un archivo en modo de lectura, puedes leer su contenido utilizando el método read(). Este método lee todo el contenido del archivo y lo devuelve como una cadena de texto.

```.py
f = open("myfile.txt", "r")
contents = f.read()
print(contents)
f.close()
```

* Escribir en un archivo: si quieres escribir en un archivo en Python, puedes abrirlo en modo de escritura utilizando el modo "w". Luego, puedes utilizar el método write() para escribir en el archivo. Por ejemplo:

```.py
f = open("myfile.txt", "w")
f.write("Hola mundo!")
f.close()
```

* Agregar contenido al final de un archivo: si quieres agregar contenido al final de un archivo en lugar de sobrescribir su contenido, puedes abrirlo en modo de adición utilizando el modo "a". Luego, puedes utilizar el método write() para agregar contenido al final del archivo. Por ejemplo:

```.py

f = open("myfile.txt", "a")
f.write("\nAñadiendo una nueva línea al final del archivo.")
f.close()

```

* Cerrar un archivo: es importante cerrar un archivo una vez que hayas terminado de trabajar con él. Puedes cerrar un archivo utilizando el método close(). Por ejemplo:

```.py
f = open("myfile.txt", "r")
contents = f.read()
f.close()
```

Es importante tener en cuenta que, cuando abres un archivo en modo de lectura o escritura, debes cerrarlo una vez que hayas terminado de trabajar con él para liberar los recursos del sistema.

## flujos

En el tema de archivos en programación, un flujo es una secuencia continua de datos que se pueden leer o escribir. Los flujos se utilizan a menudo para leer y escribir archivos, ya que permiten que un programa procese los datos de un archivo de manera secuencial, en lugar de tener que cargar todo el archivo en la memoria de una sola vez.

En Python, algunos ejemplos de flujos de entrada incluyen open(), que se utiliza para abrir un archivo para lectura, y ´sys.stdin´, que se utiliza para leer datos desde la entrada estándar (por ejemplo, el teclado). Algunos ejemplos de flujos de salida incluyen ´open()´, que también se puede utilizar para abrir un archivo para escritura, y sys.stdout, que se utiliza para escribir datos en la salida estándar (por ejemplo, la pantalla).

Los flujos se utilizan a menudo en conjunción con buffers, que son áreas de memoria que se utilizan para almacenar temporalmente los datos mientras se leen o escriben a través de un flujo. Esto puede mejorar la eficiencia de la lectura y escritura de archivos, ya que permite que el programa lea o escriba varios bytes de datos a la vez en lugar de tener que acceder al archivo un byte a la vez.

## Orientacion secuencial

La orientación secuencial en el tema de archivos en programación se refiere a la forma en que se leen y escriben los datos en un archivo. En la orientación secuencial, los datos se leen y escriben en el archivo de manera secuencial, es decir, uno después de otro en el orden en que aparecen en el archivo.