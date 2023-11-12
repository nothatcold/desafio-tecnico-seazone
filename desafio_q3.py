#3. Quais cidades têm mais avaliações?

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Carregando os arquivos desafio_ratings.csv e desafio_details.csv em dataframes
ratings_df = pd.read_csv('desafio_ratings.csv', encoding='latin1', delimiter=';')
details_df = pd.read_csv('desafio_details.csv', encoding='latin1', delimiter=';')

# Criando um novo dataframe combinando as informações dos dois arquivos usando o hotel_id e excluindo valores nulos
combined_df = pd.merge(ratings_df, details_df, on='hotel_id')

# Excluindo linhas com valores nulos na coluna 'number_of_ratings'
combined_df = combined_df.dropna(subset=['number_of_ratings'])

# Excluindo linhas onde 'number_of_ratings' é igual a 0
combined_df = combined_df[combined_df['number_of_ratings'] != 0]
combined_df.to_csv('ratings_details_merged.csv', index=False)

# Agora temos o city_name correspondente a cada avaliação
cidade_avaliacoes = combined_df.groupby('city_name')['number_of_ratings'].sum().reset_index()

# Ordenando o dataframe em ordem decrescente com base no número de avaliações
cidade_avaliacoes = cidade_avaliacoes.sort_values(by='number_of_ratings', ascending=False)

# Imprimindo o dataframe resultante
print(cidade_avaliacoes)

# Criando um gráfico
plt.figure(figsize=(10, 6))
plt.bar(cidade_avaliacoes['city_name'], cidade_avaliacoes['number_of_ratings'])
plt.xticks(rotation=80)
plt.xlabel('Cidade')
plt.ylabel('Total de Avaliações')
plt.title('Cidades com Mais Avaliações (Excluindo Valores Nulos e Zeros)')
plt.tight_layout()

# Exibindo o gráfico
plt.show()
