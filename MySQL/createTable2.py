import pandas as pd
from sqlalchemy import create_engine


class Cargar_CSV_SQL:
    def __init__(self, path, datos, name):
        self.path = path
        self.datos = datos
        self.name = name
    
    def read_CSV(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.path)
            return df
        except FileNotFoundError:
            print (f"El archivo {self.path} no existe")
    
    def convertir_SQL(self, df):
        engine = create_engine(self.datos)
        df.to_sql(
            name= self.name,
            con=engine,
            if_exists="replace",
            index=False
        )

path = "C:/Users/rdrs_/OneDrive/Documentos/GitHub/edu2/Anaconda/csv/sales_data.csv"
datos = 'mysql+mysqlconnector://root:#0795Ran$el07#@localhost/for_education'
name = "sales_data"


instance = Cargar_CSV_SQL(path,datos,name)
df = instance.read_CSV()

instance.convertir_SQL(df)














