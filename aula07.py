import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

diretorio_diabetes = r'pima-data.csv'
df = pd.read_csv(diretorio_diabetes, sep=',')

# Mostra as linhas e as colunas do arquivo
print(df.shape)
print('-' * 100)

