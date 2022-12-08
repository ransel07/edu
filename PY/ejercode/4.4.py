
# Determinar el precio de un billete de ida y vuelta en ferrocarril, conociendo la distancia a recorrer
# y sabiendo que si el número de días de estancia es superior a siete y la distancia superior
# a 800 kilómetros el billete tiene una reducción del 30%.
# El precio por kilómetro es de 2,5 pesetas.

print("PERCIO DE BILLETE DE IDA Y VUELTA EN EL FERROCARRIL")
print(" ")

dias = input("Cuantos diás = ")
distancia = input("A que diastancia esta = ")
pb = 2.5

if distancia > 800 and dias > 7:
    p_descuento = pb * 2 * distancia * 0.3
else:
    p_sin_descuento = pb * 2 * distancia


