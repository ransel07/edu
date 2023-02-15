import pandas as pd

"Crea una clase Libro con atributo Titulo, autor, editorial y año." 
"Implementa metodos para leer y escribir informacion de libros en un archivo csv "

class Libro:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
    
    def __init__(cls, record):
        for key, value in record.items():
            setattr(cls, key, value)
        Libro.count += 1

    def Escribir(self, nombre_column, descrip):
        df = pd.DataFrame()
        df[nombre_column] = descrip
    
    def ver(self):
        return self.df

r = {
    "nombre": "Avatar", 
    "año": 2009, "genero": 
    "Ciencia ficción", 
    "director": "James Cameron", 
    "actores_principales": ["Sam Worthington", "Zoe Saldana", "Sigourney Weaver"]}

# x = Libro(r)

# print (Libro.get_count())



"___________________________________________________________________"
"__________________________________________________________________"
"____________________________________________________________________"


class Empleado:
    def __init__(self, record):
        self.record = record
        for key, value in record.items():
            setattr(self, key, value)
    def DFrame(self):
        df = pd.DataFrame.from_dict(self.record)
        return df

pedro = {
    "nombres": ["Pedro", "juan"],
    "edades": [35, 33],
    "salarios": [2500, 3000] ,
    "puestos": ["Jefe de proyecto", "Jefe de local"],
    "tiempo_trabajando": [10, 12]
    }

employe = Empleado(pedro)

print(employe.DFrame())
"___________________________________________________________________"
"__________________________________________________________________"
"____________________________________________________________________"
































