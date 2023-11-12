#7. Existe alguma relação entre a nota recebida e a localização?

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Carregando o arquivo ratings_details_merged.csv em dataframe
combined_df = pd.read_csv('ratings_details_merged.csv')

# Agrupando os dados por cidade e calculando a média das notas recebidas em cada cidade
city_ratings = combined_df.groupby('city_name')['Total'].mean().reset_index()

# Ordenando o dataframe em ordem decrescente com base na média das notas
city_ratings = city_ratings.sort_values(by='Total', ascending=False)

# Criando um gráfico de barras para visualizar a média das notas por cidade
plt.figure(figsize=(10, 6))
plt.bar(city_ratings['city_name'], city_ratings['Total'])
plt.xlabel('Cidade')
plt.ylabel('Média das Notas Recebidas')
plt.title('Relação entre a Nota Recebida e a Localização (Cidade)')
plt.xticks(rotation=90)  # Rotação dos rótulos para melhor legibilidade
plt.tight_layout()

# Exibindo o gráfico
plt.show()
