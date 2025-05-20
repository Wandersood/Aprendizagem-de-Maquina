import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

diretorio_cdb = r'DadosCDB.csv'

# Forçando separador ponto e vírgula
df = pd.read_csv(diretorio_cdb, encoding='latin1', sep=';')

print(df.shape)
print('-' * 100)
print(df.info())
print('-' * 100)
print(df.head(10))
print('-' * 100)
print(df.tail(10))
print('-' * 100)
print(df.describe())
print('-' * 100)




