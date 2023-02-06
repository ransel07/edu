import pandas as pd

# Leer archivo csv
path = "C:/Users/rdrs_/OneDrive/Documentos/GitHub/Ste/Anaconda/CuentaMovimientos_.csv"
df = pd.read_csv(path)

# Eliminar columna "column_name"
df = df.drop("Unnamed: 9", axis=1)

# Guardar el archivo csv sin la columna "column_name"
df.to_csv("CuentaMovimientos_.csv", index=False)