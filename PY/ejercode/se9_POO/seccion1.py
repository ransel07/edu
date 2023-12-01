import pandas as pd

def my_function(*args):
    for arg in args:
        print(arg)
        
# my_function(1, 2, 3)

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + str(value))
        
# my_function(nombre="Juan", edad=30)

'''
Crea una clase para una lista de tareas que permita agregar, eliminar y modificar tareas, 
así como marcar tareas como completadas y listar todas las tareas.
'''

class List_Tareas:
    def __init__(self):
        self.lista=[]
    def Agregar(self,*args):
        self.lista=list(args)
    def Delete(self, dl):
        if dl in self.lista:
            self.lista.remove(dl)
    def Modify(self, md):
        if md in self.lista:
            self.lista.remove(md)
    def __str__(self):
        return str(self.lista)

lista1=List_Tareas()
lista1.Agregar('cocinar','fregar','planchar')
print(lista1)
lista1.Delete('cocinar')
print(lista1)