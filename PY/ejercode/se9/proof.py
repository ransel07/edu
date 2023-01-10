"Crea una clase Alumno que tenga los atributos nombre, edad, curso" 
"y calificaciones (una lista). Añade métodos para obtener y establecer "
"cada atributo."


class Alumno:
    def __init__(self, name, middle_name, age, curse):
        self.name = name
        self.middle_name = middle_name
        self.age = age
        self.curse = curse
        self.ratings = []



alumno = Alumno("Ransel", "Melenciano", 29, "Prime")

print (alumno.name, alumno.middle_name)

alumno.name = "Rodolfo"

print (alumno.age)