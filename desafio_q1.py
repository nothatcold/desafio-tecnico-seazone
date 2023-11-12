#1. Ordene as cidades em ordem crescente de número de listings

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Carregando o arquivo desafio_details.csv em um dataframe
details_df = pd.read_csv('desafio_details.csv', encoding='latin1', delimiter=';')
details_df.info()

# Agrupando os dados por cidade e contando o número de listings em cada cidade
cidade_listings = details_df['city_name'].value_counts().reset_index()

# Renomeando as colunas para ter nomes mais descritivos
cidade_listings.columns = ['Cidade', 'Número de Listings']

# Ordenando o dataframe em ordem decrescente com base no número de listings
cidade_listings = cidade_listings.sort_values(by='Número de Listings', ascending=True)

# Imprimindo o dataframe resultante
print(cidade_listings)

# Criando um gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(cidade_listings['Cidade'], cidade_listings['Número de Listings'])
plt.xticks(rotation=80)
plt.xlabel('Número de Listings')
plt.ylabel('Cidade')
plt.title('Número de Listings por Cidade (Ordem Crescente)')
plt.tight_layout()


# Exibindo o gráfico
plt.show()