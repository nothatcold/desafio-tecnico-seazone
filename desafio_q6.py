# 6. Existem relações entre a nota do anúncio e os recursos disponíveis no imóvel?

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Carregando o arquivo ratings_details_merged.csv em dataframe
combined_df = pd.read_csv('ratings_details_merged.csv')

# Excluindo linhas com valores nulos na coluna 'number_of_ratings'
combined_df = combined_df.dropna(subset=['number_of_ratings'])

# Excluindo linhas onde 'number_of_ratings' é igual a 0
combined_df = combined_df[combined_df['number_of_ratings'] != 0]

# Separando os recursos e eliminando valores nulos
combined_df['room_facilities'] = combined_df['room_facilities'].apply(lambda x: str(x).replace('[','').replace(']','').replace("'",'').split(','))

# Transformando a lista de recursos em linhas duplicadas
df_resources = combined_df.explode('room_facilities')

# Calculando a média de avaliações por recurso
resource_avg_ratings = df_resources.groupby('room_facilities')['number_of_ratings'].mean().reset_index()

# Ordenando o dataframe em ordem decrescente com base na média de avaliações, utilizando apenas os valores do top 50
resource_avg_ratings = resource_avg_ratings.sort_values(by='number_of_ratings', ascending=False).head(50)

# Criando um gráfico
plt.figure(figsize=(15, 8))
plt.bar(resource_avg_ratings['room_facilities'], resource_avg_ratings['number_of_ratings'])
plt.xticks(rotation=90)
plt.xlabel('Recurso')
plt.ylabel('Média de Avaliações')
plt.title('Relação entre a Nota do Anúncio e os Recursos Disponíveis no Imóvel (Top 50 Recursos)')
plt.tight_layout()

# Exibindo o gráfico
plt.show()