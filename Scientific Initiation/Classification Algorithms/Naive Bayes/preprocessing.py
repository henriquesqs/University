import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Populate our dataframe (df) skipping first row (line 0)
df = pd.read_csv('ENEM_2017.csv', skiprows=[0], low_memory=True, names=['NU_INSCRICAO','CO_MUNICIPIO_RESIDENCIA','NO_MUNICIPIO_RESIDENCIA',
                                                             'CO_UF_RESIDENCIA','NU_IDADE','TP_SEXO','TP_COR_RACA','TP_ST_CONCLUSAO',
                                                             'TP_ESCOLA','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT', 'Q001',
                                                             'Q002','Q003','Q004','Q006','Q024','Q025','REGIAO','COD_MUNICIPIO'])

df.drop(df.index[10000:4426754], inplace=True)

# Loop in df looking (and saving) for NU_NOTA_MT 
# and classifying as good (>= 518.2) or bad perfomance
math_perfomance, math_score = [], [] # blank lists

for i in df.index:
    
    math_score.append(df.at[i,'NU_NOTA_MT'])
    
    if df.at[i, 'NU_NOTA_MT'] >= 518.2: # good perfomance
        math_perfomance.append(1) 
        
    else: # bad perfomance
        math_perfomance.append(0)

# Add new column "MAT_PERFORMANCE" to our df
df['MAT_PERFORMANCE'] = math_perfomance

# Encoding our df to turn categorical columns into numerical ones
categorical_feature_mask = df.dtypes==object # categorical boolean mask
categorical_cols = df.columns[categorical_feature_mask].tolist() # filter categorical columns using mask and turn it into a list

le = preprocessing.LabelEncoder()
df[categorical_cols] = df[categorical_cols].apply(lambda col: le.fit_transform(col)) # convert categorical columns to numerical columns

# Splitting our df into attributes and labels
X = df.iloc[:, :-1].values # load our attributes values
y = math_perfomance # load labels (MAT_PERFORMANCE)

# Splitting our df into test (30% of df) and trainning sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Feature Scaling (normalization, so all features can be uniformly evaluated)
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)