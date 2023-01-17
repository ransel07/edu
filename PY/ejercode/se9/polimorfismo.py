"Crea una clase Figura con un metodo area() vacio. Luego crea dos clases hijas"
"cuadrado y triangulo que hereden de figura y sobreescriban el metodo area()"
"para calcular el area de un cuadrado y un triangulo, repectivamente. Crea una"
"lista de figuras con varios cuadros y triangulos y recorre la lista para imprimir"
"el area de cada figura."
import random

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

lista = [num for num in range(1, 11)]
random_list= [random.randint(1, 10) for num in range(11)]


def cal_area(figura):
    return figura.area()

for e, i in zip(lista, random_list):
    cuadrado = Cuadrado(e)
    triangulo = Triangulo(e, i)
    print (f"Lados de cuadraro: {e} ; Area: {cal_area(cuadrado)}")
    print (f"Base y altura: {e, i} ; Area: {cal_area(triangulo)}")