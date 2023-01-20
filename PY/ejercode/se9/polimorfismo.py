"Crea una clase Figura con un metodo area() vacio. Luego crea dos clases hijas"
"cuadrado y triangulo que hereden de figura y sobreescriban el metodo area()"
"para calcular el area de un cuadrado y un triangulo, repectivamente. Crea una"
"lista de figuras con varios cuadros y triangulos y recorre la lista para imprimir"
"el area de cada figura."
import random
import math

class Figura:
    def area(self) -> None:
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado * 4


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        base = self.base
        altura = self.altura
        return base * altura // 2

# lista = [num for num in range(1, 11)]
# random_list= [random.randint(1, 10) for num in range(11)]


# def cal_area(figura):
#     return figura.area()

# for e, i in zip(lista, random_list):
#     cuadrado = Cuadrado(e)
#     triangulo = Triangulo(e, i)
#     print (f"Lados de cuadraro: {e} ; Area: {cal_area(cuadrado)}")
#     print (f"Base y altura: {e, i} ; Area: {cal_area(triangulo)}")

"Crea una clase Automovil con un método encender() vacío. Luego, crea dos clases hijas "
"Gasolina y Electrico que hereden de Automovil y sobreescriban el método encender()" 
"para simular el encendido de un automóvil de gasolina y uno eléctrico, respectivamente. Crea" 
"una lista de automóviles con varios de gasolina y eléctricos y recorre la lista para imprimir "
"el proceso de encendido de cada uno."


class Automovil:
    def encender(self) -> None:
        pass

class Gasolina(Automovil):
    def __init__(self, auto):
        self.auto = auto
    def encender(self):
        return f"Sonido de encendido del {self.auto}"

class Electrico(Automovil):
    def __init__(self, auto):
        self.auto = auto
    def encender(self):
        return f"El {self.auto} encendió pero no se escuchó"


# for g, e in zip(dataBaseEdu.gasoline_models, dataBaseEdu.electric_models):
#     gasoline = Gasolina(g)
#     electrico = Electrico(e)
#     print (f"{gasoline.encender()} & {electrico.encender()}")

"Crea una clase Empleado con un método salario() vacío. Luego, crea dos clases hijas "
"EmpleadoFijo y EmpleadoPorHora que hereden de Empleado y sobreescriban el método "
"salario() para calcular el salario de un empleado fijo y uno por hora, respectivamente." 
"Crea una lista de empleados con varios fijos y por hora y recorre la lista para imprimir el "
"salario de cada uno."


# class Empleado:
#     def salario(self) -> None:
#         pass

# class EmpleadoFijo:
#     def __init__(self, name, salario):
#         self.name = name
#         self.salario = salario
    
#     def salary(self):
#         return f"{self.name}: {self.salario}"


# class EmpleadoPorHora:
#     def __init__(self, name, salario):
#         self.name = name
#         self.salario = salario
    
#     def salary(self):
#         return f"{self.name}: {self.salario}"

# lista = dataBaseEdu.empleadosNU
# for record in lista:
#     name = record["nombre"]
#     salary = record["salario"]
#     fijo = EmpleadoFijo(name, salary)
#     print (fijo.salary())

"Crea una clase Empleado con un método salario() vacío. Luego, crea dos clases hijas "
"EmpleadoFijo y EmpleadoPorHora que hereden de Empleado y sobreescriban el método" 
"salario() para calcular el salario de un empleado fijo y uno por hora, respectivamente." 
"Crea una lista de empleados con varios fijos y por hora y recorre la lista para imprimir" 
"el salario de cada uno."

class Empleado:
    def __init__(self, name, __salary, time):
        self.salary_ = __salary
        self.name = name
        self.time = time
    
    def salary(self):
        pass

class EmpleadoFijo(Empleado):
    def salary(self):
        return self.salary_ * self.time

class EmpleadoPorHora(Empleado):
    def salary(self):
        return self.salary_ * self.time


# numero1 = EmpleadoFijo("Rodolfo", 150, 40)

# print (numero1.salary())


"Crea una clase Figura con un método perimetro() vacío. Luego, crea tres clases hijas Cuadrado, Triangulo y Circulo que "
"hereden de Figura y sobreescriban el método perimetro() para calcular el perímetro de un" 
" cuadrado, triángulo y círculo, respectivamente. Crea una lista de figuras con varios cuadrados,"
" triángulos y círculos, y recorre la lista para imprimir el perímetro de cada una."

class Figure:
    def Perimetro():
        pass

class Square(Figure):
    def __init__(self, side):
        self.side = side

    def Perimeter(self):
        return self.side * 4

class Triangle(Figure):
    def __init__(self, sides):
        self.sides = sides

    def Perimeter(self):
        return sum(self.side1)

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def Perimeter(self):
        return math.pi * self.radius * 2



"Crea una clase Vehiculo con un método encender() vacío. Luego, crea tres clases hijas Auto," 
"Moto y Bicicleta que hereden de Vehiculo y sobreescriban el método encender() para encender" 
"un auto, moto y bicicleta, respectivamente. Crea una lista de vehículos con varios autos, motos" 
"y bicicletas, y recorre la lista para imprimir el resultado de encender cada uno de ellos."



"Crea una clase Empleado con un método salario() vacío. Luego, crea tres clases hijas EmpleadoFijo," 
"EmpleadoPorHora y EmpleadoPorComision que hereden de Empleado y sobreescriban el método salario()"
"para calcular el salario de un empleado fijo, uno por hora y uno por comisión, respectivamente. Crea"
"una lista de empleados con varios fijo"
