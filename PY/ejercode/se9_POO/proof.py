import pandas as pd


class persona:
    def __init__(self,name,lastname,type,special):
        self.name=name
        self.lastname=lastname
        self.type=type
        self.special=special
    
    def call(self):
        top=["name","lastname","type","special"]
        dt = pd.Dataframe([self.name,self.lastname,self.type,self.special])
        


name,lastname=["Juan","Isa","Pedro"],["Duarte","Mendez","Pereira"]










