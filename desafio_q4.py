#4. Quais cidades têm a maior média de avaliações? E a menor média?

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Carregando o arquivo ratings_details_merged.csv em dataframe
combined_df = pd.read_csv('ratings_details_merged.csv')

# Excluindo linhas com valores nulos ou iguais a 0 na coluna 'number_of_ratings'
combined_df = combined_df[combined_df['number_of_ratings'] != 0]
combined_df.to_csv('ratings_details_merged.csv', index=False)

# Calculando a média de avaliações por cidade
cidade_avg_reviews = combined_df.groupby('city_name')['number_of_ratings'].mean().reset_index()

# Ordenando o dataframe em ordem decrescente com base na média de avaliações
cidade_avg_reviews = cidade_avg_reviews.sort_values(by='number_of_ratings', ascending=False)

# Encontrando a cidade com a maior média de avaliações
cidade_maior_media = cidade_avg_reviews.iloc[0]

# Encontrando a cidade com a menor média de avaliações
cidade_menor_media = cidade_avg_reviews.iloc[-1]

print("Cidade com a maior média de avaliações:", cidade_maior_media['city_name'])
print("Maior média:", cidade_maior_media['number_of_ratings'])
print("\nCidade com a menor média de avaliações:", cidade_menor_media['city_name'])
print("Menor média:", cidade_menor_media['number_of_ratings'])

# Criando um gráfico
plt.figure(figsize=(10, 6))
plt.bar(cidade_avg_reviews['city_name'], cidade_avg_reviews['number_of_ratings'])
plt.xticks(rotation=80)
plt.xlabel('Cidade')
plt.ylabel('Média de Avaliações')
plt.title('Cidades com Maior e Menor Média de Avaliações')
plt.tight_layout()

# Exibindo o gráfico
plt.show()