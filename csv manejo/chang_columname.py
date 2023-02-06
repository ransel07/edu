import pandas as pd

path = "C:/Users/rdrs_/OneDrive/Documentos/GitHub/Ste/Anaconda/CuentaMovimientos_.csv"
df = pd.read_csv(path)
df = df.rename(columns={'Balance  ': 'Balance'})
df.to_csv("CuentaMovimientos_.csv", index=False)