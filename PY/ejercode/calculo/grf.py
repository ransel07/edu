import matplotlib.pyplot as plt
import numpy
import sympy 

x = sympy.Symbol("x")
f = x ** 2

# Derivada
dfdx = f.diff(x)

# Evaluar la derivada en x_0
x_0 = 1
dfdx__eval = dfdx.evalf(subs={x: x_0})

# Calcular al ecuacion de la recta tangente 
y_0 = f.evalf(subs={x: x_0})

x= numpy.linspace(-10, 10, 100)
y = x ** 2
recta_tangente = sympy.Eq(y, y_0 + dfdx__eval * (x - x_0))

print (dfdx)
print (dfdx__eval)

# plt.plot(x,y)

plt.show()





