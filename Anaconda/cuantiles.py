import numpy as np
import matplotlib.pyplot as plt

alturas = np.random.normal(1.75, 0.15, 100000)

np.quantile(alturas, [0, 1/3, 2/3, 1])

cuantiles = [(2, "Mediana"),
             (3, "Terciles"),
             (4, "Cuartiles"),
             (5, "Quintiles"),
             (10, "Deciles"),
             (100, "Percentiles")]

cortes = []
for cuantil in cuantiles:
    corte = []
    valor = 0
    for i in range(cuantil[0]-1):
        valor += 1/cuantil[0]
        corte.append(valor)         
    cortes.append(corte)

for i in range(len(cuantiles)):
    plt.figure(figsize=(7.5, 5))
    plt.title(cuantiles[i][1], size=22)
    plt.ylabel("Frecuencia", size=16)
    plt.xlabel("Alturas", size=16)
    plt.hist(alturas, 100, label="altura", color="pink")
    #print(np.quantile(alturas, [0] + cortes[i] + [1]))
    for corte in cortes[i]:
        plt.axvline(x = np.quantile(alturas, corte), label="%.2f" % corte, linewidth=3)
    if i < len(cuantiles) - 1:
        plt.legend()
    plt.show()
    print("\n"*4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    