import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


#Cria um array de 2 dimensoes: matriz 3x3
a = np.array([[1,2,3],[2,3,4],[3,4,5]])
print("Array criado:\n", a)
print("shape:", a.shape)


#criacao de uma matriz 3x2 de zeros
print("\nMatriz 3x2 de zeros:\n", np.zeros((3,2)))

#criacao de uma matriz 3x2 de uns
print("\nMatriz 3x2 de uns:\n", np.ones((3,2)))

#criacao de uma matriz identidade 3x3
print("\nMatriz 3x3 identidade:\n", np.eye(3))
print("----------------------------------------")

df = pd.read_csv('titanic.csv')
#visualizando as tres primeiras linhas
print (df.head(3))
print("\n----------------------------------------")

print(df.dtypes)
print("\n----------------------------------------")

print(df.describe())
print("\n----------------------------------------")

td = pd.read_csv('temperatura.csv')

x,y = td[['temperature']].values, td[['classification']].values

print("x:\n", x)
print("------------------------------------------")
print("y:\n", y)
print("------------------------------------------")


