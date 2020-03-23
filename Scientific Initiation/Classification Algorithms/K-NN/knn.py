import math
import random
import matplotlib
from preprocessing import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# We're going to use k = sqrt(n), 'n' num of rows in train set
k = int(round(math.sqrt(len(df.index)))) # faster than df.shape[0]

# Creating our model
model = KNeighborsClassifier(n_neighbors=k)

# Training the model using training set
model.fit(X_train,y_train)

# Predict
predicted = model.predict(X_test)

print(accuracy_score(y_test, predicted))
print(confusion_matrix(y_test,predicted))
print(classification_report(y_test,predicted))