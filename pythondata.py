from sklearn import tree
#nos permite criar um mmodelo de machine laerning chamado decision tree

clf = tree.DecisionTreeClassifier()

X = [[2,1], [8,12], [6,10], [5,4], [10,20]]# (MEDIA ESCOLAR, horas de estudo na semana)
Y = [0,1,1,0,1]

clf.fit(X, Y)
print(clf.predict([[1,1]]))
print(clf.predict([[8,14]]))


