import pandas as pd
from sqlalchemy import create_engine

path = "C:/Users/rdrs_/OneDrive/Documentos/GitHub/Ste/MySQL/productos.csv"
df = pd.read_csv(path)

engine = create_engine(
    'mysql+mysqlconnector://root:#0795Ran$el07#@localhost/for_education'
    )

df.to_sql(
    name='productos', 
    con=engine, 
    if_exists='replace', 
    index=True)








