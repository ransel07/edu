
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

estudiante = {
    "nombre" : "",
    "edad" : "",
    "promedio" : "",
    "becado" : ""
}

estudiante1 = {
    "nombre" : "Rodrigo",
    "edad" : 33,
    "promedio" : 2.9,
    "becado" : "si"
}

estudiante2 = {
    "nombre" : "ana",
    "edad" : 17,
    "promedio" : 4.0,
    "becado" : "si"
}

estudiante3 = {
    "nombre" : "Lorine",
    "edad" : 25,
    "promedio" : 2.0,
    "becado" : "no"
}

estudiante4 = {
    "nombre" : "Daneyris",
    "edad" : 30,
    "promedio" : 3.0,
    "becado" : "si"
}

estudiante["nombre"] = "David" 
estudiante["edad"] = 30 
estudiante["promedio"] = 4.0 
estudiante["becado"] = "si"

producto = {
    "nombre" : "Ram",
    "precio" : 75.5,
    "cantidad" : 1,
}

producto1 = {
    "nombre" : "Board",
    "precio" : 200.0,
    "cantidad" : 1,
}

producto2 = {
    "nombre" : "Tarjeta de Video",
    "precio" : 298.3,
    "cantidad" : 1,
}

producto3 = {
    "nombre" : "SSD m.2",
    "precio" : 93.8,
    "cantidad" : 1,
}

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

personas = [persona["edad"], persona1["edad"], persona2["edad"], persona3["edad"], persona4["edad"]]
libros_autores = [ libro["autor"],  libro1["autor"],  libro2["autor"],  libro3["autor"],  libro4["autor"]]
libros_titulo = [ libro["titulo"],  libro1["titulo"],  libro2["titulo"],  libro3["titulo"],  libro4["titulo"]]
libros_titulo1 = [ libro,  libro1,  libro2,  libro3,  libro4]
lbn = [ libro]
autor =  libro['autor']
lista_estudiantes = [ estudiante,  estudiante1,  estudiante2,  estudiante3,  estudiante4]
lista_productos = [ producto,  producto1,  producto2,  producto3]
lista_promedios = [ estudiante["promedio"],  estudiante1["promedio"],  estudiante2["promedio"],  estudiante3["promedio"],  estudiante4["promedio"]]
lista_individuos = [individuo, individuo1, individuo2, individuo3, individuo4]

for indiv in individuo4:
    print(indiv, indiv)