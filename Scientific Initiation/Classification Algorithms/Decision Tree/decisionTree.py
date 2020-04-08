import preprocessing as pp
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

clf = tree.DecisionTreeClassifier()
#clf.fit(pp.X_train,pp.y_train)

predicted = clf.predict(pp.X_test)

tree.plot_tree(clf.fit(pp.X_train,pp.y_train))

print(accuracy_score(pp.y_test, predicted))
print(confusion_matrix(pp.y_test,predicted))
print(classification_report(pp.y_test,predicted))