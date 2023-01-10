
"Crea una clase Alumno que tenga los atributos nombre, edad, curso" 
"y calificaciones (una lista). Añade métodos para obtener y establecer "
"cada atributo."


class Alumno:
    def __init__(self, name, middle_name, age):
        self.name = name
        self.middle_name = middle_name
        self.age = age
        self.ratings = []

    def get_name(self):
        return self.name

    def set_name(self):
        self.name
    
    def get_middle_name(self):
        return self.middle_name

    def set_name(self):
        self.middle_name

alumno = Alumno("Ransel", "Melenciano", 29)

def ciclo(alumno):
    switch = True
    while switch:
        pack = ["Nombre", "Apellido", "Edad"]
        call = str(input ())
        for element in pack:
            if call == element:
                return alumno.get_middle_name()

print(alumno.get_middle_name())

print(ciclo(alumno))

"Crea una clase Triangulo que tenga los atributos lado1, lado2 y "
"lado3. Añade métodos para obtener y establecer cada atributo, y también "
"un método que calcule el perímetro del triángulo."

"Crea una clase Cuenta Bancaria que tenga los atributos número de cuenta, "
"saldo y titular. Añade métodos para obtener y establecer cada atributo, y "
"también métodos para realizar depósitos y retiros de la cuenta."

"Crea una clase Libro que tenga los atributos título, autor y número de "
"páginas. Añade métodos para obtener y establecer cada atributo, y también"
"un método para mostrar la información del libro de manera formateada."