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

# # Ejemplo de uso
# lista = [range(1,10)]
# indice = binary_search(lista, 3)
# if indice == -1:
#     print("El elemento no se encuentra en la lista")
# else:
#     print("El elemento se encuentra en el índice", indice)

"__________________________________________________________________________________________________"
"Crea una función llamada busqueda_binaria que reciba como parámetros un arreglo de números enteros" 
"ordenados y un número a buscar. La función debe devolver la posición del número en el arreglo, o -1" 
"si no se encuentra."
"__________________________________________________________________________________________________"


def search_binary(lista, num):
    left_numb = 0
    right_numb = len(lista) -1
    while left_numb <= right_numb:
        middle_index = (left_numb + right_numb) // 2
        if lista[middle_index] == num:
            return middle_index
        elif lista[middle_index] < num:
            left_numb = middle_index + 1
        else:
            right_numb = middle_index - 1
    return -1

"___________________________________________________________________________"
"Crea una función llamada busqueda_binaria_recursiva que haga lo mismo que" 
"la función anterior, pero de forma recursiva."
"___________________________________________________________________________"

def busqueda():
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


"___________________________________________________________________________"
"Crea una función llamada busqueda_binaria_string que reciba como parámetros un arreglo" 
"de cadenas de caracteres ordenadas alfabéticamente y una cadena a buscar. La función debe" 
"devolver la posición de la cadena en el arreglo, o -1 si no se encuentra."
"___________________________________________________________________________"

def busqueda_binaria_string(arreglo_saludos, cadena):
    left = 0
    right = len(arreglo_saludos) - 1
    arreglo_saludos.sort()
    
    while left <= right:
        middle = (left + right)//2
        if middle == arreglo_saludos.index(cadena):
            return middle
        elif middle < arreglo_saludos.index(cadena):
            left = middle + 1
        else:
            right = middle - 1
    
    return -1

arreglo_saludos = ["Hola", "Buenos días", "Buenas tardes", "Buenas noches", "Bienvenido", 
"Gracias", "De nada", "Perdón", "Lo siento", "Adiós", "Hasta luego", "Hasta mañana", 
"Hasta pronto", "Buen viaje", "Buen fin de semana", "Buenas fiestas", 
"Feliz cumpleaños", "Felices fiestas", "Feliz Navidad", "Feliz Año Nuevo",]
cadena = "Buen viaje"

print (busqueda_binaria_string(arreglo_saludos, cadena))

"___________________________________________________________________________"
"Crea una función llamada busqueda_binaria_Mayusculas que reciba como parámetros un arreglo"
"de cadenas de caracteres ordenadas alfábeticamente en mayúsculas y una cadena a buscar tambien en mayúscula. "
"La función debe devolver la posición de la cadena en el arreglo, o -1 si no se encuentra."
"___________________________________________________________________________"

def busqueda_binaria_Mayusculas(arreglo_mayus, cadena):
    left = 0
    right = len(arreglo_mayus) - 1
    while left <= right:
        middle = (left + right) // 2
        if middle == arreglo_mayus.index(cadena):
            return cadena
        elif middle < arreglo_mayus.index:
            left = middle + 1
        else:
            right = middle - 1
    


"___________________________________________________________________________"
"Crea una función llamada busqueda_binaria_fechas que reciba como parámetros un arreglo"
"de variables de tipo fecha ordenadas cronológicamente y una fecha a buscar. "
"Una fecha se puede representar con un registro que contenga los campos día, mes y año." 
"La función debe devolver la posición de la fecha en el arreglo, o -1 si no se encuentra."
"___________________________________________________________________________"


"___________________________________________________________________________"
"Crea una función llamada busqueda_binaria_estructura que reciba como parámetros un arreglo "
"de cualquier tipo de estructura ordenada y un elemento a buscar. La función debe devolver la" 
"posición del elemento en el arreglo, o -1 si no se encuentra."
"___________________________________________________________________________"

