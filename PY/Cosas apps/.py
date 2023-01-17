import matplotlib.pyplot as plt

# Ejemplo de vectores
x = [1, 2]
y = [3, 4]
u = [1, 2]
v = [3, 4]

# Crear un plano cartesiano
plt.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=1)
plt.xlim([0, 5])
plt.ylim([0, 5])
plt.show()