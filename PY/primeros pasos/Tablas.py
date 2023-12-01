#Primero instalamos la biblioteca tabulada usando pip install en la línea de comando:
#"pip install tabulate"
#Luego importamos la función tabular de la biblioteca tabular en nuestro código:
#"from tabulate import tabulate"

from tabulate import tabulate                                                        
                                                                                    

x = int(input("Juan = "))
y = int(input("Christopher = "))
z = int(input("Randel = "))
k = int(input("Sebastian = "))
i = int(input("Ransel = "))

fila_superior = ["Nombres", "Puntos"]
mi_tabla = ["Juan Jose", "Christopher", "Randel", "Sebastian", "Ransel"], [x, y, z, k, i]

print(tabulate(mi_tabla, headers = fila_superior))