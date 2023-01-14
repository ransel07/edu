
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

"Crea una clase Persona con atributos name y age y metodos hi() y birday()."
"El metodo hi() debe imprimir un mensaje que diga hola, mi nombre es [nombre]"
"y el metodo birtday debe sumar 1 a la edad de la persona."

class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hi(self):
        return f"Saludos, mi nombre es {self.name} y tengo "
    
    def Birtday(self):
        self.age += 1
        return self.age

carl = Persona("Carlo", 30)

# print (carl.hi() ,carl.Birtday(), carl.Birtday())


"Crea una clase CuentaBancaria con atributos nombre_titular y saldo. "
"Agrega métodos depositar() y retirar() para modificar el saldo "
"de la cuenta. Asegúrate de que no se pueda retirar más dinero del que "
"se tiene en la cuenta."

class CuentaBancaria:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
    
    def Deposit(self, amount):
        return self.cash + amount
    def Withdrawal(self, amount):
        if self.cash >= 1 and amount <= self.cash:
            return self.cash - amount
        else:
            return "No tiene balance suficiente para la transaccion"

cuenta = CuentaBancaria("Juan", 5000)

# print(cuenta.Deposit(6000))
# print(cuenta.Withdrawal(3000))
# print(cuenta.Withdrawal(3000))
# print(cuenta.Withdrawal(5500))

"Crea una clase Auto con atributos marca, modelo y año. "
"Agrega un método encender() que imprima El auto está encendiendo "
"y un método apagar() que imprima El auto está apagando."

class Electric_Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def on(self):
        return f"The {self.model} is on"
    def off(self):
        return f"The {self.model} is off"
Tesla = Electric_Car("Tesla", "Model S", 2023)

# print (Tesla.on())
# print (Tesla.off())


"Crea una clase Estudiante con atributos nombre y calificaciones "
"(una lista de números). Agrega un método promedio() que calcule el "
"promedio de las calificaciones del estudiante."

class Estudiante:
    def __init__(self, name, parcial1, parcial2, parcial3) -> None:
        self.name = name
        self.parcial1 = parcial1
        self.parcial2 = parcial2
        self.parcial3 = parcial3
        self.ratings = [self.parcial1, self.parcial2, self.parcial3]
    
    def average(self):
        average = sum(self.ratings)/len(self.ratings)
        return average

first = Estudiante("Martinez", 90, 88, 80)
# print (first.average())

class Estudiante: # Chat GPT
    def __init__(self, name, ratings) -> None:
        self.name = name
        self.ratings = ratings
    
    def average(self):
        average = sum(self.ratings)/len(self.ratings)
        return average

first = Estudiante("Martinez", [90, 88, 80])

"Crea una clase Reloj con atributos hora y minutos. "
"Agrega métodos mostrar_hora() y ajustar_hora() para mostrar la "
"hora y cambiarla, respectivamente. Asegúrate de que la hora siempre "
"esté en un formato válido (entre 0 y 23 para las horas y entre 0 y 59 "
"para los minutos)."

class Reloj:
    def __init__(self, hour, minute):
        if -1 < hour  < 24 and -1 < minute < 60:
            self.hour = hour
            self.minute = minute
        else:
            print (f"The Parameter {hour} or {minute} not valide")

    def show(self):
        return f"{self.hour}:{self.minute}"
    
    def set_time(self, hour, minute):
        if -1 < hour  < 24 and -1 < minute < 60:
            h = self.hour = hour
            m = self.minute = minute
            return f"{h}:{m}"
        else:
            print (f"The Parameter {hour} or {minute} not valide")


hour = 12
minute = 30

atomic_hour = Reloj(hour, minute)
# print (atomic_hour.show())
# print (atomic_hour.set_time(50, 20))


print(id(atomic_hour))
