import pandas as pd

path = "C:/Users/rdrs_/OneDrive/Documentos/GitHub/Ste/CuentaMovimientos_2320755313_2023-02-05 1124.csv"
df = pd.read_csv(path, encoding='ISO-8859-1')
df.to_csv(path, index=False, encoding='utf-8-sig')

