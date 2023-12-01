import pandas as pd

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def suma(self):
        poo = self.a + self.b
        return poo

# dig1 = input("Introduzca el primer numero = ")
# dig2 = input("Introduzca el sergundo numero = ")
# instancia = Calculadora(dig1, dig2).suma()
# print(instancia)

class estudiante():
    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age
        self.etiqueta="Estudiante"

    def call(self):
        dt1=[[self.name,self.lastname,self.age]]
        encabezado=["Nombre","Apellido", "Edad"]
        dataf=pd.DataFrame(dt1, columns=encabezado)
        return dataf

class Profesor():
    def __init__(self,name,lastname,age,especialidad):
        self.name=name
        self.lastname=lastname
        self.age=age
        self.especialidad=especialidad
        self.etiqueta="Profesor"

class Cursos:
    def __init__(self, asignatura):
        self.asignatura = asignatura
        self.cupos = 25
        self.count = 0

    def asignar(self, data2):

        self.cupos = self.cupos - 1
        self.count = self.count + 1

        top = ["Nombre", "Cupo", "inscritos"]
        dt = [self.asignatura, self.cupos, self.count]
        data1 = pd.DataFrame(data=dt, columns=top)
        ndt = pd.concat([data1,data2], axis=1, ignore_index=True)
        return ndt
    
    def proof(self):

        self.cupos = self.cupos - 1
        self.count = self.count + 1

        top = ["Nombre", "Cupo", "inscritos"]
        dt = [self.asignatura, self.cupos, self.count]
        data1 = pd.DataFrame(data=dt, columns=top)
        return data1



juan = estudiante("Juan","Duarte",20).call()
pedro = estudiante("Pedro","Monette",21).call()


matematicas = Cursos("Matematicas")
fisica = Cursos("Fisica")
geometria = Cursos("Geometria A")

print(matematicas.proof())
print(juan)

