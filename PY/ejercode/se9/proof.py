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
    
    def Name_Position(self, name, position):
        print (self.name)
        print (self.position)

emp1 = Employee("Juan", 40000, "Analista de Datos")

Employee.Name_Position()