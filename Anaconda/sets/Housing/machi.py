import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10.0, 8.0)
import seaborn as sns
from scipy import stats
from scipy.stats import norm


train = pd.read_csv("C:/Users/rdrs_/OneDrive/Documentos/GitHub/Ste/Anaconda/sets/Housing/train.csv")
test = pd.read_csv("C:/Users/rdrs_/OneDrive/Documentos/GitHub/Ste/Anaconda/sets/Housing/test.csv")

head_train = train.head(5)
# info_train = train.info()

# REVISAR SI EL CONJUNTO DE DATOS TIENE UN VALOR FALTANTE

train.columns[train.isnull().any()]

# PORCENTAJE DE VALORES FALTANTES

miss = train.isnull().sum()/len(train)
miss = miss[miss > 0]
miss.sort_values(inplace = True)

# VISUALIZACION DE VALORES PERDIDOS
miss = miss.to_frame() # Convierte los valores en "DataFrame"
miss.columns = ["count"]
miss.index.names = ["Name"]
miss["Name"] = miss.index

# GRAFICAR CONTEO DE VALORES PERDIDOS
sns.set(style="whitegrid", color_codes=True)
sns.barplot(x = "Name", y = "count", data=miss)
plt.xticks(rotation = 90)
plt.show()

# PRECIO DE VENTA
# sns.distplot(train["SalePrice"])

# OBLICUIDAD O ESTANDARIZACION (DESVIASION ESTANDAR)
# print ("La Oblicuidad del SalePrice es {}".format(train["SalePrice"].skew()))

# AHORA TRANSFORMANDO LA VARIABLE OBJETIVO
target = np.log(train["SalePrice"])
print ("Skewness is", target.skew())
sns.distplot(target)

# SEPARACION DE VARIABLE

numeric_data = train.select_dtypes(include = [np.number])
cat_data = train.select_dtypes(exclude = [np.number])
numericos = numeric_data.shape[1]
categoricos = cat_data.shape[1]
print (numericos + categoricos)
print ("Numericos: {}, Categoricos: {}".format(numericos,categoricos))

del numeric_data["Id"]

# GRAFICO DE CORRELACION

corr = numeric_data.corr()
sns.heatmap(corr)

# 

print (corr["SalePrice"].sort_values(ascending=False)[:15], "\n")
print ("================================")
print (corr["SalePrice"].sort_values(ascending=False)[-5:])

train["OverallQual"].unique()
# array([7, 6, 8, 5, 9, 4, 10, 3, 1, 2])

# COMPROBEMO EL PRECIO MEDIO POR CALIDAD Y GRAFIQUEMOSLO
pivot = train.pivot_table(index="OverallQual", vaules="SalePrice", aggfunc=np.median)
pivot.sort









































