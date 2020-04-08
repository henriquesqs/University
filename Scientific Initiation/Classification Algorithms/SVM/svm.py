import preprocessing as pp
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Creating and trainning our model
svc = SVC(kernel='linear')
svc.fit(pp.X_train, pp.y_train)

# Predict
predicted = svc.predict(pp.X_test)

print(accuracy_score(pp.y_test, predicted))
print(confusion_matrix(pp.y_test,predicted))
print(classification_report(pp.y_test,predicted))

