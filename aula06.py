import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

diretorio_clientes = r'perfil_clientes.csv'
df = pd.read_csv(diretorio_clientes,sep=';')


#mostra as linhas e as colunas do arquivo
print(df.shape)
print('-'*100)

#mostra as informacoes dos tipos dos dados
print(df.info())
print('-'*100)

#mostra as 5 primeiras linhas e as 5 ultimas linhas
print(df.head(10))
print('-'*100)
print(df.tail())
print('-'*100)

#mostras as estatisticas dos dados
print(df.describe())
print('-'*100)

#inverter os eixos da tabela de resultados(transpose) e o round arredonda os valores
print(round(df.describe().transpose(),2))
print('-'*100)

#conta quantos dados tem uma coluna especifica
contagem_dados = df['estado_civil'].value_counts()
print (contagem_dados)
print('-'*100)

#conta quantos dados tem uma coluna especifica e mostra o grafico
grafico = contagem_dados.plot(kind='barh',figsize=(12,8),color='red')
plt.title('Estado Civil')
plt.xlabel('Contagem')
plt.ylabel('Estado Civil')
plt.show()
print(grafico)
print('-'*100)

# Tabela cruzada com outra variável categórica "Região"
tabela_cruzada = pd.crosstab(df['estado_civil'], df['região'])
print(tabela_cruzada)
print('-'*100)

#Agregação de Dados
agregacao = df.groupby('estado_civil')['idade'].max()
print(agregacao)
print('-'*100)

#dados duplicados
duplicados = df[df.duplicated()]
print(duplicados)
print('-'*100)

''