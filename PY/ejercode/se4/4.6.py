# Se desea realizar una estadística de los pesos de los alumnos de un colegio de acuerdo
# a la siguiente tabla:

# Alumnos de menos de 40 kg.
# Alumnos entre 40 y 50 kg.
# Alumnos de más de 50 y menos de 60 kg.
# Alumnos de más o igual a 60 kg.

# La entrada de los pesos de los alumnos se terminará cuando se introduzca el valor centinela -99.
# Al final se desea obtener cuántos alumnos hay en cada uno de los baremos.


cont_1 = 0
cont_2 = 0
cont_3 = 0
cont_4 = 0

pesos = int(input("Introduce el peso = "))

while pesos != -99:

    if pesos < 40:
        cont_1 = cont_1 + 1

    elif 40 <= pesos <= 50:
        cont_2 = cont_2 + 1

    elif 50 < pesos < 60:
        cont_3 = cont_3 + 1

    elif pesos >= 40:
        cont_4 = cont_4 + 1
    
    pesos = int(input("Introduce el peso = "))


print ("Alumnos de menos de 40 kg", cont_1)   
print("Cantidad de Alumnos entre 40 y 50 kg = ", cont_2)
print("Cantidad de Alumnos de más de 50 y menos de 60 kg = ", cont_3)
print("Cantidad de Alumnos de más o igual a 60 kg = ", cont_4)