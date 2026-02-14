from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

#DADOS: anos na empresa, horas de trabalho
x = [[6,8], [2,5], [5,8], [3,7], [1,9], [10, 5], [9,5], [8,6]]
Y = [1,0,1,0,1,2,2,2] #2: toma um aviso 1: continua 0: demitido
model.fit(x, Y)

print(model.predict([[10,9]]))
print(model.predict([[7,7]]))
print(model.predict([[1,7]]))




