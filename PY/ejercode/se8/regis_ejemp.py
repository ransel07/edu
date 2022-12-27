
persona = {
    'nombre': 'Juan',
    'edad': 35,
    'direccion': 'Calle Falsa 123'
}

pelicula = {
    'titulo': 'Star Wars',
    'director': 'George Lucas',
    'ano': 1977,
    'actores': ['Mark Hamill', 'Harrison Ford', 'Carrie Fisher']
}

persona1 = {
    "nombre" : "Rodrigo",
    "edad" : 33,
    "direccion" : "una calle hay numero algo"
}

persona2 = {
    "nombre" : "ana",
    "edad" : 28,
    "direccion" : "calle 13"
}

persona3 = {
    "nombre" : "Lorine",
    "edad" : 25,
    "direccion" : "zona colonial"
}

persona4 = {
    "nombre" : "Daneyris",
    "edad" : 30,
    "direccion" : "kings Landing"
}



# Crea un procedimiento llamado "imprimir_persona" que reciba como parámetro una variable de tipo "persona" y muestre en 
# pantalla los valores de sus campos. 

def imprimir_persona(persona):
    print(persona["nombre"])
    print(persona["edad"])
    print(persona["direccion"])

persona["nombre"] = "Ransel"
persona["edad"] = 27
persona["direccion"] = "calle puerto rico #14"

libro = {
    'titulo': 'El señor de los anillos',
    'autor': 'J.R.R. Tolkien',
    'año': 1954,
    'genero': 'Fantasía'
}

libro1 = {
    'titulo': 'El señor de los anillos',
    'autor': 'J.R.R. Tolkien',
    'año': 1954,
    'genero': 'Fantasía'
}

libro2 = {
    'titulo': 'Game of Throne',
    'autor': 'George R. R. Martin',
    'año': 1996,
    'genero': 'Fantasía Medival'
}

libro3 = {
    'titulo': 'Los juegos del hambre',
    'autor': 'Suzanne Collins',
    'año': 2008,
    'genero': 'Ficción adulto joven'
}

libro4 = {
    'titulo': 'Danza de dragones',
    'autor': 'George R. R. Martin',
    'año': 2011,
    'genero': 'Fantasía Medival'
}

libro["titulo"] = "Harry Potter y el Prisionero de Askaban"
libro["autor"] = "J.K. Rolling"
libro["año"] = 1999

# Crea un registro llamado "estudiante" que contenga los campos "nombre", "edad", "promedio" y "becado". Luego, 
# crea una variable de este tipo de registro y asígnale valores a sus campos.

#                           Lista de Registros de Estudiantes

estudiantes = [{"2018-5542" : {"nombre" : "Ansel","edad" : "27", "examen 1" : 90,"examen 2" : 30,"examen 3" : 70, "becado" : "Si"}},
{"2018-3054" : {"nombre" : "Rodrigo","edad" : "33","examen 1" : 70,"examen 2" : 60,"examen 3" : 70, "becado" : "no"}},
{"2018-2045" : {"nombre" : "ana","edad" : "17","examen 1" : 72,"examen 2" : 79,"examen 3" : 85,"becado" : "no"}},
{"2018-5563" : {"nombre" : "Lorine","edad" : "25","examen 1" : 81,"examen 2" : 89,"examen 3" : 90, "becado" : "no"}}, 
{"2018-5564" : {"nombre" : "Daneyris","edad" : "30","examen 1" : 94,"examen 2" : 95,"examen 3" : 99, "becado" : "no"}},
{"2018-9657" : {"nombre" : "Magnolia", "edad" : "20","examen 1" : 87,"examen 2" : 85,"examen 3" : 79, "becado" : "no"}},
{"2017-1257" : {"nombre" : "Marco", "edad" : "26","examen 1" : 92,"examen 2" : 70,"examen 3" : 59, "becado" : "no"}},
{"2018-7257" : {"nombre" : "Layla", "edad" : "26","examen 1" : 85,"examen 2" : 75,"examen 3" : 87, "becado" : "no"}},
{"2018-4537" : {"nombre" : "Loyda", "edad" : "25","examen 1" : 99,"examen 2" : 97,"examen 3" : 99,"becado" : "si"}},
{"2019-1234": {"nombre": "Juan", "edad": "22", "examen 1": 85, "examen 2": 95, "examen 3": 80, "becado": "No"}},
{"2019-5678": {"nombre": "Ana", "edad": "20", "examen 1": 75, "examen 2": 85, "examen 3": 90, "becado": "no"}},
{"2018-9101": {"nombre": "Pedro", "edad": "25", "examen 1": 95, "examen 2": 85, "examen 3": 80, "becado": "No"}},
{"2018-1213": {"nombre": "Laura", "edad": "24", "examen 1": 85, "examen 2": 75, "examen 3": 90, "becado": "no"}},
{"2019-2424": {"nombre": "Mario", "edad": "23", "examen 1": 80, "examen 2": 90, "examen 3": 85, "becado": "No"}},
{"2018-3434": {"nombre": "Sandra", "edad": "21", "examen 1": 95, "examen 2": 80, "examen 3": 75, "becado": "no"}},
{"2019-4545": {"nombre": "Pablo", "edad": "26", "examen 1": 96, "examen 2": 75, "examen 3": 80, "becado": "No"}},
{"2018-5656": {"nombre": "Raquel", "edad": "25", "examen 1": 85, "examen 2": 95, "examen 3": 70, "becado": "no"}},
{"2019-6767": {"nombre": "Gustavo", "edad": "24", "examen 1": 75, "examen 2": 85, "examen 3": 90, "becado": "No"}},
{"2018-7878": {"nombre": "Gloria", "edad": "23", "examen 1": 95, "examen 2": 80, "examen 3": 75, "becado": "no"}}]


#                                                     Registros de Estudiantes indexados

EstudiantesIndex = {"2018-5542" : {"nombre" : "Ansel","edad" : "27", "examen 1" : 90,"examen 2" : 30,"examen 3" : 70, "becado" : "Si"},
"2018-3054" : {"nombre" : "Rodrigo","edad" : "33","examen 1" : 70,"examen 2" : 60,"examen 3" : 70, "becado" : "no"},
"2018-2045" : {"nombre" : "ana","edad" : "17","examen 1" : 72,"examen 2" : 79,"examen 3" : 85,"becado" : "no"},
"2018-5563" : {"nombre" : "Lorine","edad" : "25","examen 1" : 81,"examen 2" : 89,"examen 3" : 90, "becado" : "no"}, 
"2018-5564" : {"nombre" : "Daneyris","edad" : "30","examen 1" : 94,"examen 2" : 95,"examen 3" : 99, "becado" : "no"},
"2018-9657" : {"nombre" : "Magnolia", "edad" : "20","examen 1" : 87,"examen 2" : 85,"examen 3" : 79, "becado" : "no"},
"2017-1257" : {"nombre" : "Marco", "edad" : "26","examen 1" : 92,"examen 2" : 70,"examen 3" : 59, "becado" : "no"},
"2018-7257" : {"nombre" : "Layla", "edad" : "26","examen 1" : 85,"examen 2" : 75,"examen 3" : 87, "becado" : "no"},
"2018-4537" : {"nombre" : "Loyda", "edad" : "25","examen 1" : 99,"examen 2" : 97,"examen 3" : 99,"becado" : "si"},
"2019-1234" : {"nombre": "Juan", "edad": "22", "examen 1": 85, "examen 2": 95, "examen 3": 80, "becado": "No"},
"2019-5678" : {"nombre": "Ana", "edad": "20", "examen 1": 75, "examen 2": 85, "examen 3": 90, "becado": "no"},
"2018-9101" : {"nombre": "Pedro", "edad": "25", "examen 1": 95, "examen 2": 85, "examen 3": 80, "becado": "No"},
"2018-1213" : {"nombre": "Laura", "edad": "24", "examen 1": 85, "examen 2": 75, "examen 3": 90, "becado": "no"},
"2019-2424" : {"nombre": "Mario", "edad": "23", "examen 1": 80, "examen 2": 90, "examen 3": 85, "becado": "No"},
"2018-3434" : {"nombre": "Sandra", "edad": "21", "examen 1": 95, "examen 2": 80, "examen 3": 75, "becado": "no"},
"2019-4545" : {"nombre": "Pablo", "edad": "26", "examen 1": 96, "examen 2": 75, "examen 3": 80, "becado": "No"},
"2018-5656" : {"nombre": "Raquel", "edad": "25", "examen 1": 85, "examen 2": 95, "examen 3": 70, "becado": "no"},
"2019-6767" : {"nombre": "Gustavo", "edad": "24", "examen 1": 75, "examen 2": 85, "examen 3": 90, "becado": "No"},
"2018-7878" : {"nombre": "Gloria", "edad": "23", "examen 1": 95, "examen 2": 80, "examen 3": 75, "becado": "no"}}

#                           Registros de EmpleadosTecIndex

EmpladosTecIndex = {"Juan": {"edad": 25, "salario": 1500, "puesto": "Programador", "tiempo_trabajando": 2, "tiene_seguro": True},
"Ana": {"edad": 30, "salario": 2000, "puesto": "Analista de datos", "tiempo_trabajando": 5, "tiene_seguro": True},
"Pedro": {"edad": 35, "salario": 2500, "puesto": "Jefe de proyecto", "tiempo_trabajando": 10, "tiene_seguro": False},
"Sofía": {"edad": 40, "salario": 3000, "puesto": "Gerente de TI", "tiempo_trabajando": 15, "tiene_seguro": True},
"Mario": {"edad": 45, "salario": 3500, "puesto": "Director de TI", "tiempo_trabajando": 20, "tiene_seguro": False},
"Laura": {"edad": 50, "salario": 4000, "puesto": "Consultora de TI", "tiempo_trabajando": 25, "tiene_seguro": True},
"Pablo": {"edad": 55, "salario": 4500, "puesto": "Experto en seguridad informática", "tiempo_trabajando": 30, "tiene_seguro": False},
"Rocío": {"edad": 60, "salario": 5000, "puesto": "Experto en bases de datos", "tiempo_trabajando": 35, "tiene_seguro": True},
"Miguel": {"edad": 65, "salario": 5500, "puesto": "Experto en machine learning", "tiempo_trabajando": 40, "tiene_seguro": False},
"Carla": {"edad": 70, "salario": 6000, "puesto": "Experto en inteligencia artificial", "tiempo_trabajando": 40, "tiene_seguro": False}}

#                           Registros de Productos

producto = {9534 : {"nombre" : "Ram", "precio" : 75.5,"cantidad disponible" : 50,}}
producto1 = {7985 : {"nombre" : "Board", "precio" : 200.0, "cantidad disponible" : 9,}}
producto2 = {3215 : {"nombre" : "Tarjeta de Video", "precio" : 298.3, "cantidad disponible" : 15,}}
producto3 = {2458 : {"nombre" : "SSD m.2", "precio" : 93.8, "cantidad disponible" : 33,}}
producto4 = {2358 : {"nombre" : "SSD Kingston 250GB", "precio" : 110.30, "cantidad disponible" : 30,}}
producto5 = {6547 : {"nombre" : "Hard Drive 2T", "precio" : 145.99, "cantidad disponible" : 53,}}
producto6 = {8756 : {"nombre" : "Disipador Coolermaster", "precio" : 50.5, "cantidad disponible" : 15,}}

#                           Registros de Individuos

individuo = {
    "nombre" : "Rodrigo",
    "edad" : 22,
    "pais" : "EE.UU.",
    "estado" : "Florida"
}

individuo1 = {
    "nombre" : "Ana",
    "edad" : 30,
    "pais" : "Colombia",
    "estado" : "Bogota"
}

individuo2 = {
    "nombre" : "Marta",
    "edad" : 40,
    "pais" : "España",
    "estado" : "Madrid"
}

individuo3 = {
    "nombre" : "Jonathan",
    "edad" : 29,
    "pais" : "Rep. Dom.",
    "estado" : "Santo Domingo"
}

individuo4 = {
    "nombre" : "Vanessa",
    "edad" : 30,
    "pais" : "Rep. Dom.",
    "estado" : "Santo Domingo"
}

#                                          LISTAS de Registro de empleados

empleados = [{204600003: {'nombre': 'Ana', "cargo": "ventas", "salario": 35000, "seguro social": 454545, 'edad': 30, 'direccion': 'Calle Falsa 456'}},
{204600004: {'nombre': 'Pedro', "cargo": "recursos humanos", "salario": 27000, "seguro social": 345345, 'edad': 25, 'direccion': 'Calle #9 789'}},
{204600005: {'nombre': 'Laura', "cargo": "administración", "salario": 32000, "seguro social": 757575, 'edad': 28, 'direccion': 'Calle Falsa 159'}},
{204600006: {'nombre': 'Mario', "cargo": "soporte técnico", "salario": 25000, "seguro social": 242424, 'edad': 29, 'direccion': 'Calle Empanada 357'}},
{204600007: {'nombre': 'Sandra', "cargo": "ventas", "salario": 30000, "seguro social": 131313, 'edad': 24, 'direccion': 'Calle De verdad 258'}},
{204600008: {'nombre': 'Pablo', "cargo": "recursos humanos", "salario": 29000, "seguro social": 121212, 'edad': 23, 'direccion': 'Calle Falsa 369'}},
{204600009: {'nombre': 'Raquel', "cargo": "administración", "salario": 31000, "seguro social": 101010, 'edad': 27, 'direccion': 'Calle Falsa 159'}},
{204600011: {'nombre': 'Carla', "cargo": "soporte técnico", "salario": 26000, "seguro social": 90909, 'edad': 22, 'direccion': 'Calle Falsa 159'}},
{204600012: {'nombre': 'Gustavo', "cargo": "ventas", "salario": 33000, "seguro social": 88888, 'edad': 26, 'direccion': 'Calle Falsa 555'}},
{204600013: {'nombre': 'Gloria', "cargo": "recursos humanos", "salario": 30000, "seguro social": 77777, 'edad': 29, 'direccion': 'Calle Falsa 666'}},
{204600014: {'nombre': 'Hector', "cargo": "administración", "salario": 34000, "seguro social": 66666, 'edad': 24, 'direccion': 'Calle Falsa 777'}},

]

#                                           LISTAS DE REGISTROS

personas_edades = [persona["edad"], persona1["edad"], persona2["edad"], persona3["edad"], persona4["edad"]]
personas = [persona, persona1, persona2, persona3, persona4]
libros_autores = [ libro["autor"],  libro1["autor"],  libro2["autor"],  libro3["autor"],  libro4["autor"]]
libros_titulo = [ libro["titulo"],  libro1["titulo"],  libro2["titulo"],  libro3["titulo"],  libro4["titulo"]]
libros_titulo1 = [libro, libro1, libro2, libro3, libro4]
lbn = [ libro]
autor =  libro['autor']
lista_productos = [ producto,  producto1,  producto2,  producto3, producto4, producto5, producto6]
lista_individuos = [individuo, individuo1, individuo2, individuo3, individuo4]








