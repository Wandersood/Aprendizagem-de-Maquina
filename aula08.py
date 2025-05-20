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


# Dados fictícios
bancos = ['Itaú', 'Santander', 'BB', 'BTG', 'Master', 'PagSeguro', 'XP']
lucros = [10.51, 3.78, 8.77, 3.3, 1.068, 0.631, 1.18]

# Estilo do seaborn
sns.set(style="whitegrid")

# Criar gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x=lucros, y=bancos, palette="Blues_d")

plt.xlabel('Lucro Líquido (em bilhões)')
plt.ylabel('Banco')
plt.title('Lucro Líquido por Banco')
plt.tight_layout()
plt.show()
