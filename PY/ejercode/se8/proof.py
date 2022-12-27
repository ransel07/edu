empleados = [{"nombre": "Juan", "edad": 25, "salario": 1500, "puesto": "Programador", "tiempo_trabajando": 2},
{"nombre": "Ana", "edad": 30, "salario": 2000, "puesto": "Analista de datos", "tiempo_trabajando": 5},
{"nombre": "Pedro", "edad": 35, "salario": 2500, "puesto": "Jefe de proyecto", "tiempo_trabajando": 10},
{"nombre": "Sofía", "edad": 40, "salario": 3000, "puesto": "Gerente de TI", "tiempo_trabajando": 15},
{"nombre": "Mario", "edad": 45, "salario": 3500, "puesto": "Director de TI", "tiempo_trabajando": 20}]

indice = {}

intro = "ana"

for id, element in enumerate(empleados):
    indice[element["nombre"]] = id

data = empleados[indice[intro.title()]]
for attribute in data:
    print(f"{attribute} : {data[attribute]}")

#for i in indice:
    #print(f"{i} : {indice[i]}")

