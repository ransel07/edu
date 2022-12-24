
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

#                           Registros de Estudiantes

estudiante = {
    "nombre" : "Ransel",
    "edad" : "27",
    "examen 1" : 90,
    "examen 2" : 30,
    "examen 3" : 70,
    "promedio" : 2.0,
    "becado" : "Si"
}

estudiante1 = {
    "nombre" : "Rodrigo",
    "edad" : 33,
    "examen 1" : 70,
    "examen 2" : 60,
    "examen 3" : 70,
    "promedio" : 2.9,
    "becado" : "si"
}

estudiante2 = {
    "nombre" : "ana",
    "edad" : 17,
    "examen 1" : 70,
    "examen 2" : 79,
    "examen 3" : 85,
    "promedio" : 4.0,
    "becado" : "si"
}

estudiante3 = {
    "nombre" : "Lorine",
    "edad" : 25,
    "examen 1" : 80,
    "examen 2" : 89,
    "examen 3" : 90,
    "promedio" : 2.0,
    "becado" : "no"
}

estudiante4 = {
    "nombre" : "Daneyris",
    "edad" : 30,
    "examen 1" : 90,
    "examen 2" : 95,
    "examen 3" : 99,
    "promedio" : 2.1,
    "becado" : "si"
}


#                           Registros de Productos

producto = {"nombre" : "Ram", "precio" : 75.5,"cantidad disponible" : 50,}
producto1 = {"nombre" : "Board", "precio" : 200.0, "cantidad disponible" : 10,}
producto2 = {"nombre" : "Tarjeta de Video", "precio" : 298.3, "cantidad disponible" : 15,}
producto3 = {"nombre" : "SSD m.2", "precio" : 93.8, "cantidad disponible" : 33,}
producto4 = {"nombre" : "SSD Kingston 250GB", "precio" : 110.30, "cantidad disponible" : 30,}
producto5 = {"nombre" : "Hard Drive 2T", "precio" : 145.99, "cantidad disponible" : 53,}
producto6 = {"nombre" : "Disipador Coolermaster", "precio" : 50.5, "cantidad disponible" : 15,}

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

#                                          Registro de empleados

empleado = {3 : {'nombre': 'Juan', "cargo" : "contabilidad", "salario" : 23000, "seguro social" : 542542,'edad': 35, 'direccion': 'Calle Falsa 123'}}
empleado1 = {1 : {"nombre" : "Rodrigo", "cargo" : "RRHH", "salario" : 53000, "seguro social" : 809574, "edad" : 33, "direccion" : "una calle hay numero algo"}}
empleado2 = {2 : { "nombre" : "ana", "cargo" : "mantenimiento", "salario" : 20000, "seguro social" : 152634, "edad" : 28, "direccion" : "calle 13"}}
empleado3 = {4 : {"nombre" : "Lorine", "cargo" : "monitoreo", "salario" : 27000, "seguro social" : 121350, "edad" : 25, "direccion" : "zona colonial"}}
empleado4 = {5 : {"nombre" : "Daneyris", "cargo" : "soporte tecnico", "salario" : 22000, "seguro social" : 304020, "edad" : 30, "direccion" : "kings Landing"}}

#                                           LISTAS DE REGISTROS

personas_edades = [persona["edad"], persona1["edad"], persona2["edad"], persona3["edad"], persona4["edad"]]
personas = [persona, persona1, persona2, persona3, persona4]
libros_autores = [ libro["autor"],  libro1["autor"],  libro2["autor"],  libro3["autor"],  libro4["autor"]]
libros_titulo = [ libro["titulo"],  libro1["titulo"],  libro2["titulo"],  libro3["titulo"],  libro4["titulo"]]
libros_titulo1 = [libro, libro1, libro2, libro3, libro4]
lbn = [ libro]
autor =  libro['autor']
estudiantes = [ estudiante,  estudiante1,  estudiante2,  estudiante3,  estudiante4]
lista_productos = [ producto,  producto1,  producto2,  producto3, producto4, producto5, producto6]
lista_promedios = [ estudiante["promedio"],  estudiante1["promedio"],  estudiante2["promedio"],  estudiante3["promedio"],  estudiante4["promedio"]]
lista_individuos = [individuo, individuo1, individuo2, individuo3, individuo4]
empleados = [empleado, empleado1, empleado2, empleado3, empleado4]


def promedio():
    for elemento in estudiantes:
        examen1 = int(elemento["examen 1"])        
        examen2 = int(elemento["examen 2"])
        examen3 = int(elemento["examen 3"])
        sum =  examen1 + examen2 + examen3
        base4 = sum/25
        promedio = base4/3
        elemento["promedio"] = round(promedio, 1)    # Redondeo del "promedio" que se introduce en el "elemento["promedio"]"
        
        
promedio()

estudiantes = [ estudiante,  estudiante1,  estudiante2,  estudiante3,  estudiante4]


