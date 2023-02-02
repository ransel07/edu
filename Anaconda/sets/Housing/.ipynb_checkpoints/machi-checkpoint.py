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
info_train = train.info()

# REVISAR SI EL CONJUNTO DE DATOS TIENE UN VALOR FALTANTE

train.columns[train.isnull().any()]

# PORCENTAJE DE VALORES FALTANTES

miss = train.isnull().sum()/len(train)
miss = miss[miss > 0]
miss.sort_vaules(inplace=True)
miss





































