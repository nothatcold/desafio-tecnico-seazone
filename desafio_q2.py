#2. Ordene as cidades em ordem decrescente de metros quadrados;

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Carregando o arquivo desafio_details.csv em um dataframe
details_df = pd.read_csv('desafio_details.csv', encoding='latin1', delimiter=';')

# Removendo linhas com valores nulos na coluna 'room_surface_in_m2'
details_df = details_df.dropna(subset=['room_surface_in_m2'])

# Agrupando os dados por cidade e calculando a média de metros quadrados
cidade_avg_sqm = details_df.groupby('city_name')['room_surface_in_m2'].mean().reset_index()

# Ordenando o dataframe em ordem decrescente com base na média de metros quadrados
cidade_avg_sqm = cidade_avg_sqm.sort_values(by='room_surface_in_m2', ascending=False)

# Imprimindo o dataframe resultante
print(cidade_avg_sqm)

# Criando um gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(cidade_avg_sqm['city_name'], cidade_avg_sqm['room_surface_in_m2'])
plt.xticks(rotation=80)
plt.xlabel('Média de Metros Quadrados')
plt.ylabel('Cidade')
plt.title('Média de Metros Quadrados por Cidade (Ordem Decrescente)')
plt.tight_layout()

# Exibindo o gráfico
plt.show()
