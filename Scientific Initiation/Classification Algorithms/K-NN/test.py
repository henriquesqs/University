import numpy as np
import pandas as pd
import matplotlib
from sklearn import metrics
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Populate our dataframe (df) skipping first row (line 0)
df = pd.read_csv('ENEM_2017.csv', skiprows=[0], low_memory=True, names=['NU_INSCRICAO','CO_MUNICIPIO_RESIDENCIA','NO_MUNICIPIO_RESIDENCIA',
                                                             'CO_UF_RESIDENCIA','NU_IDADE','TP_SEXO','TP_COR_RACA','TP_ST_CONCLUSAO',
                                                             'TP_ESCOLA','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT', 'Q001',
                                                             'Q002','Q003','Q004','Q006','Q024','Q025','REGIAO','COD_MUNICIPIO'])


df.drop(df.index[5000:4426754], inplace=True)

# Create new column named 'range' which separates NU_NOTA_Mt by ranges
df['range_encoded'] = pd.cut(df['NU_NOTA_MT'], [350, 400, 450, 500, 550, 600, 650, 700, 750, 800], include_lowest=True, right=False)

# Copying our new column to a list
score_range = []
score_range = df['range_encoded']

# Encoding our df to turn categorical columns of 'object' type into numerical ones
categorical_feature_mask = df.dtypes==object # categorical boolean mask
categorical_cols = df.columns[categorical_feature_mask].tolist() # filter categorical columns using mask and turn it into a list

le = preprocessing.LabelEncoder()
df[categorical_cols] = df[categorical_cols].apply(lambda col: le.fit_transform(col)) # convert categorical columns to numerical columns

# Encoding our df to turn categorical columns of 'category' type into numerical ones
categorical_columns = df.select_dtypes(['category']).columns
df[categorical_columns] = df[categorical_columns].apply(lambda x: x.cat.codes)

# To better understand our range codification
df['range'] = score_range

matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt

x = df['Q006']
y = df['Q001']

plt.title('Grafico')
plt.ylabel('Q001')
plt.xlabel('Q006')

xpositions = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
xlabels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']

ypositions = (0,1,2,3,4,5,6,7)
ylabels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

plt.xticks(xpositions, xlabels)
plt.yticks(ypositions, ylabels)

plt.colorbar()
plt.scatter(x, y)

plt.show()