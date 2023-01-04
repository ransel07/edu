
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

#                                lista de empleados

empleadosNU = [{"nombre": "Juan", "edad": 25, "salario": 1500, "puesto": "Programador", "tiempo_trabajando": 2},
{"nombre": "Ana", "edad": 30, "salario": 2000, "puesto": "Analista de datos", "tiempo_trabajando": 5},
{"nombre": "Pedro", "edad": 35, "salario": 2500, "puesto": "Jefe de proyecto", "tiempo_trabajando": 10},
{"nombre": "Sofía", "edad": 40, "salario": 3000, "puesto": "Gerente de TI", "tiempo_trabajando": 15},
{"nombre": "Mario", "edad": 45, "salario": 3500, "puesto": "Director de TI", "tiempo_trabajando": 20},
{"nombre": "Laura", "edad": 50, "salario": 4000, "puesto": "Consultora de TI", "tiempo_trabajando": 25},
{"nombre": "Pablo", "edad": 55, "salario": 4500, "puesto": "Experto en seguridad informática", "tiempo_trabajando": 30},
{"nombre": "Rocío", "edad": 60, "salario": 5000, "puesto": "Experto en bases de datos", "tiempo_trabajando": 35},
{"nombre": "Miguel", "edad": 65, "salario": 5500, "puesto": "Experto en machine learning", "tiempo_trabajando": 40},
{"nombre": "Carla", "edad": 70, "salario": 6000, "puesto": "Experto en inteligencia artificial", "tiempo_trabajando": 40},
{"nombre": "Fernando", "edad": 35, "salario": 2500, "puesto": "Jefe de proyecto", "tiempo_trabajando": 10},
{"nombre": "Gloria", "edad": 40, "salario": 3000, "puesto": "Gerente de TI", "tiempo_trabajando": 15},
{"nombre": "Hector", "edad": 45, "salario": 3500, "puesto": "Director de TI", "tiempo_trabajando": 20},
{"nombre": "Irina", "edad": 50, "salario": 4000, "puesto": "Consultora de TI", "tiempo_trabajando": 25},
{"nombre": "Javier", "edad": 55, "salario": 4500, "puesto": "Experto en seguridad informática", "tiempo_trabajando": 30},
{"nombre": "Frack", "edad": 45, "salario": 5500, "puesto": "Experto en seguridad informática", "tiempo_trabajando": 30},
{"nombre": "Rose", "edad": 37, "salario": 5000, "puesto": "Experto en seguridad informática", "tiempo_trabajando": 30}]


#                           Registros de Individuos


dominicanos = [{"nombre" : "Jonathan","edad" : 29,"pais" : "Rep. Dom.","estado" : "Santo Domingo"},
{"nombre" : "Vanessa","edad" : 30,"pais" : "Rep. Dom.","estado" : "Santo Domingo"},
{"nombre" : "Luis","edad" : 40,"pais" : "Rep. Dom.","estado" : "Santo Domingo"},
{"nombre" : "Carla","edad" : 35,"pais" : "Rep. Dom.","estado" : "Santo Domingo"},
{"nombre" : "Andrea","edad" : 25,"pais" : "Rep. Dom.","estado" : "Santo Domingo"},
{"nombre" : "Roberto","edad" : 32,"pais" : "Rep. Dom.","estado" : "Santo Domingo"},
{"nombre" : "Sandra","edad" : 28,"pais" : "Rep. Dom.","estado" : "Santo Domingo"},
{"nombre" : "Javier","edad" : 37,"pais" : "Rep. Dom.","estado" : "Santo Domingo"},
{"nombre" : "Claudia","edad" : 31,"pais" : "Rep. Dom.","estado" : "Santo Domingo"},
{"nombre" : "Mario","edad" : 33,"pais" : "Rep. Dom.","estado" : "Santo Domingo"},
{"nombre" : "Ana","edad" : 30,"pais" : "Rep. Dom.","estado" : "Santo Domingo"},
{"nombre" : "Pablo","edad" : 29,"pais" : "Rep. Dom.","estado" : "Santo Domingo"}]

#                                          LISTAS de Registro de empleados

empleadosCode = [{204600003: {'nombre': 'Ana', "cargo": "ventas", "salario": 35000, "seguro social": 454545, 'edad': 30, 'direccion': 'Calle Falsa 456'}},
{204600004: {'nombre': 'Pedro', "cargo": "recursos humanos", "salario": 27000, "seguro social": 345345, 'edad': 25, 'direccion': 'Calle #9 789'}},
{204600005: {'nombre': 'Laura', "cargo": "administración", "salario": 32000, "seguro social": 757575, 'edad': 28, 'direccion': 'Calle Falsa 159'}},
{204600006: {'nombre': 'Mario', "cargo": "soporte técnico", "salario": 25000, "seguro social": 242424, 'edad': 29, 'direccion': 'Calle Empanada 357'}},
{204600007: {'nombre': 'Sandra', "cargo": "ventas", "salario": 30000, "seguro social": 131313, 'edad': 24, 'direccion': 'Calle De verdad 258'}},
{204600008: {'nombre': 'Pablo', "cargo": "recursos humanos", "salario": 29000, "seguro social": 121212, 'edad': 23, 'direccion': 'Calle Falsa 369'}},
{204600009: {'nombre': 'Raquel', "cargo": "administración", "salario": 31000, "seguro social": 101010, 'edad': 27, 'direccion': 'Calle Falsa 159'}},
{204600011: {'nombre': 'Carla', "cargo": "soporte técnico", "salario": 26000, "seguro social": 90909, 'edad': 22, 'direccion': 'Calle Falsa 159'}},
{204600012: {'nombre': 'Gustavo', "cargo": "ventas", "salario": 33000, "seguro social": 88888, 'edad': 26, 'direccion': 'Calle Falsa 555'}},
{204600013: {'nombre': 'Gloria', "cargo": "recursos humanos", "salario": 30000, "seguro social": 77777, 'edad': 29, 'direccion': 'Calle Falsa 666'}},
{204600014: {'nombre': 'Hector', "cargo": "administración", "salario": 34000, "seguro social": 66666, 'edad': 24, 'direccion': 'Calle Falsa 777'}},]

#                                           LISTAS DE REGISTROS de peliculas

movie = [{"nombre": "Avatar", "año": 2009, "genero": "Ciencia ficción", "director": "James Cameron", "actores_principales": ["Sam Worthington", "Zoe Saldana", "Sigourney Weaver"]},
{"nombre": "Titanic", "año": 1997, "genero": "Drama romántico", "director": "James Cameron", "actores_principales": ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"]},
{"nombre": "Harry Potter y la piedra filosofal", "año": 2001, "genero": "Fantasía", "director": "Chris Columbus", "actores_principales": ["Daniel Radcliffe", "Emma Watson", "Rupert Grint"]},
{"nombre": "El señor de los anillos: La comunidad del anillo", "año": 2001, "genero": "Fantasía", "director": "Peter Jackson", "actores_principales": ["Elijah Wood", "Ian McKellen", "Orlando Bloom"]},
{"nombre": "Indiana Jones y el templo maldito", "año": 1984, "genero": "Aventuras", "director": "Steven Spielberg", "actores_principales": ["Harrison Ford", "Kate Capshaw", "Jonathan Ke Quan"]},
{"nombre": "La terminal", "año": 2004, "genero": "Comedia", "director": "Steven Spielberg", "actores_principales": ["Tom Hanks", "Catherine Zeta-Jones", "Diego Luna"]},
{"nombre": "La la land", "año": 2016, "genero": "Musical", "director": "Damien Chazelle", "actores_principales": ["Ryan Gosling", "Emma Stone", "John Legend"]},
{"nombre": "La reina de las nieves", "año": 2013, "genero": "Animación", "director": "Chris Buck", "actores_principales": ["Kristen Bell", "Idina Menzel", "Jonathan Groff"]}]

movie2 = [{"nombre": "El señor de los anillos", "año": 2001, "genero": "Fantasía", "duración": "3h 48min", "calificación": 9.0},
{"nombre": "Matrix", "año": 1999, "genero": "Ciencia ficción", "duración": "2h 16min", "calificación": 8.7},
{"nombre": "Forrest Gump", "año": 1994, "genero": "Drama", "duración": "2h 22min", "calificación": 8.8},
{"nombre": "Titanic", "año": 1997, "genero": "Drama", "duración": "3h 14min", "calificación": 7.7},
{"nombre": "Indiana Jones", "año": 1981, "genero": "Aventura", "duración": "1h 55min", "calificación": 8.2},
{"nombre": "Pulp Fiction", "año": 1994, "genero": "Thriller", "duración": "2h 34min", "calificación": 8.9},
{"nombre": "Star Wars: Episodio V", "año": 1980, "genero": "Ciencia ficción", "duración": "2h 4min", "calificación": 8.7},
{"nombre": "El rey león", "año": 1994, "genero": "Animación", "duración": "1h 28min", "calificación": 8.5},
{"nombre": "El club de la pelea", "año": 1999, "genero": "Drama", "duración": "2h 19min", "calificación": 8.3},
{"nombre": "La vida es bella", "año": 1997, "genero": "Comedia", "duración": "2h 2min", "calificación": 8.6},
{"nombre": "El señor de los anillos: La comunidad del anillo", "año": 2001, "genero": "Acción", "duración": "3h 48min", "calificación": 8.9},
{"nombre": "Matrix", "año": 1999, "genero": "Ciencia ficción", "duración": "2h 16min", "calificación": 8.7},
{"nombre": "El rey león", "año": 1994, "genero": "Animación", "duración": "1h 28min", "calificación": 8.5},
{"nombre": "Forrest Gump", "año": 1994, "genero": "Comedia dramática", "duración": "2h 22min", "calificación": 8.8},
{"nombre": "Titanic", "año": 1997, "genero": "Drama romántico", "duración": "3h 15min", "calificación": 7.8},
{"nombre": "Avatar", "año": 2009, "genero": "Ciencia ficción", "duración": "2h 42min", "calificación": 7.9},
{"nombre": "Piratas del Caribe: La maldición del perla negra", "año": 2003, "genero": "Aventura", "duración": "2h 23min", "calificación": 8.0},
{"nombre": "Harry Potter y la piedra filosofal", "año": 2001, "genero": "Aventura", "duración": "2h 32min", "calificación": 7.6}]

#                               Registros de Productos

productos = [
{"nombre" : "Laptop", "marca" : "HP", "modelo" : "Elitebook", "precio" : 750.5, "cantidad disponible" : 50},
{"nombre" : "Teclado", "marca" : "Logitech", "modelo" : "G513", "precio" : 99.99, "cantidad disponible" : 75},
{"nombre" : "Monitor", "marca" : "Dell", "modelo" : "U2415", "precio" : 249.99, "cantidad disponible" : 25},
{"nombre" : "Mouse", "marca" : "Razer", "modelo" : "Deathadder", "precio" : 69.99, "cantidad disponible" : 100},
{"nombre" : "CPU", "marca" : "AMD", "modelo" : "Ryzen 9 5900X", "precio" : 499.99, "cantidad disponible" : 50},
{"nombre" : "Motherboard", "marca" : "Asus", "modelo" : "ROG Strix B550-E", "precio" : 199.99, "cantidad disponible" : 75},
{"nombre" : "RAM", "marca" : "Corsair", "modelo" : "Vengeance LPX 16GB DDR4", "precio" : 75.5, "cantidad disponible" : 100},
{"nombre" : "SSD", "marca" : "Samsung", "modelo" : "970 Evo 500GB", "precio" : 109.99, "cantidad disponible" : 50},
{"nombre" : "Case", "marca" : "Phanteks", "modelo" : "Eclipse P400A", "precio" : 99.99, "cantidad disponible" : 75},
{"nombre" : "Power Supply", "marca" : "EVGA", "modelo" : "750W SuperNOVA", "precio" : 119.99, "cantidad disponible" : 25},
{"nombre" : "Monitor", "marca" : "Dell", "modelo" : "U2718Q", "precio" : 699.0, "cantidad disponible" : 20},
{"nombre" : "Laptop", "marca" : "Lenovo", "modelo" : "ThinkPad X1 Carbon", "precio" : 1499.0, "cantidad disponible" : 15},
{"nombre" : "Impresora", "marca" : "HP", "modelo" : "OfficeJet Pro 7740", "precio" : 299.99, "cantidad disponible" : 10},
{"nombre" : "Router", "marca" : "Netgear", "modelo" : "Nighthawk R7000", "precio" : 199.99, "cantidad disponible" : 25},
{"nombre" : "Smartphone", "marca" : "Apple", "modelo" : "iPhone 12", "precio" : 849.99, "cantidad disponible" : 40},
{"nombre" : "Altavoces", "marca" : "JBL", "modelo" : "Charge 4", "precio" : 149.95, "cantidad disponible" : 35},
{"nombre" : "Tablet", "marca" : "Samsung", "modelo" : "Galaxy Tab S7", "precio" : 649.99, "cantidad disponible" : 30},
{"nombre" : "Cámara de fotos", "marca" : "Canon", "modelo" : "EOS 5D Mark IV", "precio" : 2499.0, "cantidad disponible" : 20},
{"nombre" : "Consola de videojuegos", "marca" : "Sony", "modelo" : "PlayStation 5", "precio" : 499.99, "cantidad disponible" : 15},
{"nombre" : "Smartwatch", "marca" : "Fitbit", "modelo" : "Versa 3", "precio" : 199.95, "cantidad disponible" : 25}
]

#                                           LISTAS DE REGISTROS

personas = [persona, persona1, persona2, persona3, persona4]
libros_autores = [ libro["autor"],  libro1["autor"],  libro2["autor"],  libro3["autor"],  libro4["autor"]]
libros_titulo = [ libro["titulo"],  libro1["titulo"],  libro2["titulo"],  libro3["titulo"],  libro4["titulo"]]
libros_titulo1 = [libro, libro1, libro2, libro3, libro4]
lbn = [ libro]
autor =  libro['autor']









