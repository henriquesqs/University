from preprocessing import *
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Creating and trainning our model
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Predict
predicted = gnb.predict(X_test)

print(accuracy_score(y_test, predicted))
print(confusion_matrix(y_test,predicted))
print(classification_report(y_test,predicted))