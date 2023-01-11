
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

# print(alumno.get_middle_name())

# print(ciclo(alumno))

"Crea una clase Empleado que tenga los atributos nombre, salario y "
"cargo. Añade métodos para obtener y establecer cada atributo, y también"
"un método para mostrar el nombre y el cargo del empleado."

class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
    
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_salary(self):
        return self.salary
    def set_salary(self, salary):
        self.salary = salary
    def get_position(self, position):
        return self.position
    def set_position(self, position):
        self.position = position
    
    def Name_Position(self):
        print ("Nombre: ",self.name)
        print ("Puesto: ",self.position)

emp1 = Employee("Juan", 40000, "Analista de Datos")

# emp1.Name_Position()



"Crea una clase Triangulo que tenga los atributos lado1, lado2 y "
"lado3. Añade métodos para obtener y establecer cada atributo, y también "
"un método que calcule el perímetro del triángulo."

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def get_lado1(self, lado1):
        self.lado1 = lado1
    def get_lado1(self, lado2):
        self.lado2 = lado2
    def get_lado1(self, lado3):
        self.lado3 = lado3
    
    def Perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

triangle = Triangulo(3, 4, 2)

# print(triangle.Perimetro())



"Crea una clase Cuenta Bancaria que tenga los atributos número de cuenta, "
"saldo y titular. Añade métodos para obtener y establecer cada atributo, y "
"también métodos para realizar depósitos y retiros de la cuenta."

class Cuenta_Bancaria:
    def __init__(self, numb, cash, name):
        self.numb = numb
        self.cash = cash
        self.name = name
    
    def get_lado1(self, numb):
        self.numb = numb
    def get_lado1(self, cash):
        self.cash = cash
    def get_lado1(self, name):
        self.name = name
    
    def Trans(self):
        self.cash -= monto
        print (self.cash)

client = Cuenta_Bancaria(100239453, 1000, "Ransel")
monto = 50

# client.Trans()

"Crea una clase llamada Cuadrado que tenga un atributo y metodo para obtener"
"y establecer su valor. Agregar tambien un metodo que calcule el areca del"
"Cuadrado"

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def get_lado(self, lado):
        return self.lado
    def set_lado(self, lado):
        self.lado = lado

    def Area(self):
        return self.lado*4

cuadrado = Cuadrado(4)

cuadrado.set_lado(5)

# print(cuadrado.Area())

