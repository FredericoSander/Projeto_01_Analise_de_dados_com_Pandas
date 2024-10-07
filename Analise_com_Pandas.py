import pandas as pd

netflix_titles = "C:/Users/desk/Desktop/vexpenses/netflix_titles.csv"

df = pd.read_csv(netflix_titles)

print("Questão 01: Quais coluna estão presente no dataset?")

print()
print("No arquivo estão presente as seguinte colunas:")
print(df.info())# Este código exibe as informações gerais do Dataframe (Colunas, tipos, etc...)
# O dataset possui 12 colunas sendo elas show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description.

print() # Organizar a apresentação
print("-------------------------------------------------------------------------------------------------")  #Organizar a apresentação
print() # Organizar a apresentação

print("Questão 02: Quantos filmes estão disponíveis na Netflix?")
print()# Organizar a apresentação
# Este código verifica se a string 'Movie' aparece em cada registro da coluna 'type' sem diferenciar letras maiusculas de minúsculas. 
# A função .sum() conta quantas string Movie aparece na coluna.
total_movies = df['type'].str.contains('Movie',case=False, na=False).sum()
print(f"Na plataforma da Netflix existem {total_movies} filmes disponiveis!") # 
# O data set possui 6131 filmes essa informação pode ser obtida por meio da variável total_movies:

print() # Organizar a apresentação
print("-------------------------------------------------------------------------------------------------")  # Organizar a apresentação
print() # Organizar a apresentação

print("Questão 03: Quem são os 5 diretores com mais filmes e séries na plataforma?")
print() # Organizar a apresentação
# O director_df cria o dataframe de director e utiliza a função dropna() para eliminar entradas nulas, a função str.split() separa os nomes dos diretores em uma lista e a função explode()
# criar uma nova linha para cada diretor, permitindo a contagem de diretóres unicos.
director_df = df['director'].dropna().str.split(', ').explode()
# A variável diretores_contagem utiliza a função value_counts() para contar e retornar uma série com os nomes e a quantidade de vezes que um mesmo nome aparece na colunas dos diretores.
diretores_contagem = director_df.value_counts() 
# A função head() em pandas retorna por padrão as 5 primeiras linhas contendo o nome dos diretor e o numero de vezes em que aparece,
# para retornar um valor diferente de 5, basta passar o valor no argumento da função.
top_5_diretores = diretores_contagem.head() 
print("Os 5 diretores com mais filmes e séries na plataforma são:")
print(top_5_diretores) # Imprime a variável top_5_diretores.
# Os 5 diretores com mais filmes e series são Rajiv Chilaka com 22 ocorrências, Jan Suter com 21 ocorrências, Raúl Campos com 19 ocorrências, Marcus Raboy 16 ocorrências e Suhas Kadav 16 ocorrências.

print() # Organizar a apresentação
print("-------------------------------------------------------------------------------------------------")  # Organizar a apresentação
print() # Organizar a apresentação

print("Questão 04: Quais diretores também atuaram como atores em sua produções?")
print() # Organizar a apresentação
# O director_df cria o dataframe de director e utiliza a função dropna() para eliminar entradas nulas, a função str.split() separa os nomes dos diretores em uma lista e a função explode()
# criar uma nova linha para cada diretor, permitindo a contagem de diretóres unicos.
director_df = df['director'].dropna().str.split(', ').explode()
# A função unique() é utilizada para para retornar uma lista de elentos unicos do dataframe director_df.
unique_directors = director_df.unique()
# pd.Dataframe criar um novo DataFrame a partir da lista de atores únicos obtidos anteriormente.
df_unique_directors = pd.DataFrame(unique_directors, columns=['unique_directors'])
# O actors_df recebe o dataframe criado de forma semenlhante a criação do director_df.
actors_df = df['cast'].dropna().str.split(', ').explode()
# A função unique() é utilizada para para retornar uma lista de elentos unicos do dataframe actors_df.
unique_actors = actors_df.unique()
# O código pd.Dataframe criar um novo DataFrame a partir da lista de atores únicos obtidos anteriormente.
df_unique_actors = pd.DataFrame(unique_actors, columns=['unique_actors'])
# O código a seguir é utilizado para encontrar a interseção entre duas listas de nomes, diretores e atores. 
diretores_atores = set(df_unique_directors['unique_directors']) & set(df_unique_actors['unique_actors'])
# Função df_diretores_atores cria um novo dataframe para armazernar os nomes dos diretores que também são atores. 
df_diretores_atores = pd.DataFrame(diretores_atores, columns=['diretores_atores'])
print("A seguir segue a relação dos diretores também que atuaram como atores em suas produções:")
print(df_diretores_atores) # imprime o dataframe df_diretores_atores

print() # Organizar a apresentação
print("-------------------------------------------------------------------------------------------------")  # Organizar a apresentação
print() # Organizar a apresentação

print("Questão 05: Qual é a proporção de filmes em relação a serie na Netflix?") 
print() # Organizar a apresentação
# Este código verifica se a string 'TV Show' aparece em cada registro da coluna 'type' sem diferenciar letras maiusculas de minúsculas. 
# A função .sum() conta quantas string 'TV Show' existem na coluna.
total_tvshow = df['type'].str.contains('TV Show',case=False, na=False).sum()
# Na variável proporção de filmes a proporção de filmes em relação a series é obtida pela divisão da variável total filmes por total_tv_show
# O código a seguir reaproveita a variavel total_movies criada na questão 02.
proporcoa_filmes = total_movies / total_tvshow 
print(f"Para cada serie adicionada na Netflix existe uma proporção de {proporcoa_filmes:.2f} filmes adicionados!") # imprime a resposta contextualizada.

print() # Organizar a apresentação
print("-------------------------------------------------------------------------------------------------")  # Organizar a apresentação
print() # Organizar a apresentação

print("Questão 06: Apresente uma relação de 05 anos em houve o maior número de lançamentos, ordenado pelo número de lançamentos:")
print() # Organizar a apresentação
# Este código cria o dataframe release_contagem e a função value_counts realiza a contagem dos anos neste dataframe
release_contagem = df['release_year'].value_counts()
# A função head() em pandas retorna por padrão as 5 primeiras linhas do dataframe release_contagem contendo o ano como indice e o numero de lançamento de cada ano.
top_5_anos_release = release_contagem.head()
print("Os 5 anos com maior numero de lançamentos foram:") # imprime a resposta contextualizada.
print(top_5_anos_release) # imprime a resposta contextualizada.

print() # Organizar a apresentação
print("-------------------------------------------------------------------------------------------------")  # Organizar a apresentação
print() # Organizar a apresentação

print("Questão 07: Apresente uma relação de 05 anos em que mais filmes foram adicionados a plataforma.")
print()
# O código abaixo cria um dataframe, a função pd.to_datetime(df['date_added'], errors='coerce') é utilizada para converte a coluna 'date_added' em um formato de data e hora.
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# O código a seguir cria o dataframe filmes_df contendo registros relacionados a filmes, a função df['type'] == 'Movie'] é utilizada para obter as linhas onde a coluna 'type' é igual a 'Movie'
# e a função .copy() cria uma cópia deste subconjunto em filme_df.
filmes_df = df[df['type'] == 'Movie'].copy()
# O código filmes_df['date_added'].dt.year é utilizado para extrair o ano de uma data contida na coluna date_added do datframe e armazenar este informaão em uma nova coluna chamada 'year_added'
filmes_df['year_added'] = filmes_df['date_added'].dt.year
# O método .dropna(), remove os valores nulos do dataframe, o argumento (subset=['year_added']) especifica que a verificação de valores nulos deve ser feita na coluna 'year_added'.
filmes_df = filmes_df.dropna(subset=['year_added'])
# O método .value_counts é utilizado para contar a ocorrência de cada valor único na coluna 'year_added'
added_contagem = filmes_df['year_added'].value_counts()
# O método head() retorna por padrão os 5 primeiro registros da serie 'added_contagem'. 
top_5_anos_added = added_contagem.head()
print("Os 5 anos com mais adição de filmes na plataforma foram:") # imprime a resposta contextualiza.
print(top_5_anos_added) # imprime a resposta contextualiza.

print() # Organizar a apresentação
print("-------------------------------------------------------------------------------------------------")  # Organizar a apresentação
print() # Organizar a apresentação

print("Questão 08: Em qual ano foram lançados mais filmes.")
print()
# O código filmes_df['release_year'].value_counts() é utilizado para contar quantos filmes forma lançados em cada ano com base na coluna 'release_year'.
contagem_filmes = filmes_df['release_year'].value_counts()
# O método idxmax() retorna o rótulo ou indice do valor máximo da serie 'contagem_filmes'.
ano_max_release = contagem_filmes.idxmax()
# O método .max() retorna o valor máximo dos elementos da serie 'contagem_filmes'.
quant_max_filmes = contagem_filmes.max()
print(f"O ano com o maior números de lançamentos foi {ano_max_release}, com {quant_max_filmes} novos filmes lançados.") # imprime a resposta contextualiza.

print() # Organizar a apresentação
print("-------------------------------------------------------------------------------------------------")  # Organizar a apresentação
print() # Organizar a apresentação

print("Questão 09: Apresente uma relação com os 5 atores que mais atuaram em filmes:")
print()

# O código movie_df = df[df['type'].str.contains('movie', case=False, na=False)], filtra o dataframe para selecionar apenas produções do tipo 'filme'.
movie_df = df[df['type'].str.contains('movie',case=False, na=False)]
# O código all_actors = movie_df['cast'].str.split(', ').explode().dropna(), processa a coluna 'cast' e extrai do dataframe filtrado anteiormente, 
# para criar uma lista dos atores que aparecem nos filmes separando por linha o método '.expleode() e eliminando os valores nulos com a função .dropna().
all_actors = movie_df['cast'].str.split(', ').explode().dropna()
# O código all_actors.value_counts() conta quantas vezes cada ator aparece na lista all_actors.
actors_count = all_actors.value_counts()
# O método head() retorna por padrão os 5 primeiro registros da serie 'actors_count'. 
top_5_actor_movie = actors_count.head()
print(top_5_actor_movie) # imprime a resposta contextualiza.

print() # Organizar a apresentação
print("-------------------------------------------------------------------------------------------------")  # Organizar a apresentação
print() # Organizar a apresentação

print("Questão 10: Quais são os 10 paises com maior número de produções de filmes e series?")
print()
# O código df['country'].str.split(', ').explode() extrai a coluna country do Dataframe df a função .str.split(', ') separa os valores da coluna em uma lista de países
#  utilizando como referencia os separadoras(', '), já a função explode() transforma a lista de países, onde cada item da lista irá criar uma linha. 
all_countries = df['country'].str.split(', ').explode()
# O código all_countries.value_counts() conta quantas vezes cada país aparece na lista all_countries
country_counts = all_countries.value_counts()
# O método head() retorna as 10 primeiras linhas com o maior numero de produções.
top_10_countries = country_counts.head(10)
print("Os 10 países com maior número de produções são:") # imprime a resposta contextualiza.
print(top_10_countries) # imprime a resposta contextualiza.

print() # Organizar a apresentação
print("-------------------------------------------------------------------------------------------------") # Organizar a apresentação
print() # Organizar a apresentação

print("Questão 11: Quantas series de tv temos na plataforma da Netflix?")
print()
# A variável total_tvshow implementa o código df['type'].str.contains('TV Show',case=False, na=False) para verificar se a string 'TV Show' aparece em cada registro da coluna 'type'.
# Para isso são utilizados os argumentos da função case=False para ignorar a difenciação entre maiusculas e minusculas e na=False para ignorar os valores de NAN.
# A função .sum() conta quantas string 'TV Show' existem na coluna.
total_tvshow = df['type'].str.contains('TV Show',case=False, na=False).sum()
print(f"Na plataforma da Netflix existem {total_tvshow} series disponiveis!") # imprime a resposta contextualiza.
# O data set possui 2676 series essa informação pode ser obtida por meio da variável total_tvshow:

print() #Organizar a apresentação
print("-------------------------------------------------------------------------------------------------") #Organizar a apresentação
print() #Organizar a apresentação


print("Questão 12: Em qual ano foram produzido mais series de TV.")
print()
# O código a seguir cria o dataframe tvshow_df contendo registros relacionados a series, a função df['type'] == 'TV Show'] é utilizada para obter as linhas onde a coluna 'type' é igual a 'TV Show"
# e a função .copy() cria uma cópia deste subconjunto em tvshow_df.
tvshow_df = df[df['type'] == 'TV Show'].copy()
# Este código conta quantas vezes o valor distinto ano aparece na coluna release_year e retorna uma serie na qual o ano é o indice e o numero de series foram lançadas no ano
contagem_tvshow = tvshow_df['release_year'].value_counts() # 
# Este código retorna o ano em aque houve o maior numero de series lançadas
ano_max_release_tvshow = contagem_tvshow.idxmax()
# Este código retorna o maior valor presente na serie contagem_tvshow.max().
quant_max_tvshow = contagem_tvshow.max()
print(f"O ano com o maior números de lançamentos de series foi {ano_max_release_tvshow}, com {quant_max_tvshow} novas series lançadas.") # imprime a resposta contextualiza.

print() #Organizar a apresentação
print("-------------------------------------------------------------------------------------------------") #Organizar a apresentação
print() #Organizar a apresentação

print("Questão 13: Quais são as 10 classificações indicativa de faixa etária da plataforma com mais conteúdos associados?")
print()
# O código df['rating'].str.split(', ').explode() extrai a coluna country do Dataframe df, a função .str.split(', ') separa os valores da coluna em uma lista de 'rating' (classificações)
#  utilizando como referencia os separadoras(', '), já a função explode() transforma a lista de 'rating', onde cada item da lista irá gerar uma nova linha. 
all_rating = df['rating'].str.split(', ').explode()
# Este código conta quantas vezes uma classificação distinta aparece na coluna 'rating'
rating_counts = all_rating.value_counts()
# O método head() retorna as 10 primeiras linhas de classificações com o maior numero de ocorrência.
top_10_rating = rating_counts.head(10)
print("As top 10 classificações indicativa com mais conteúdos são:")# imprime a resposta contextualiza.
print(top_10_rating)# imprime a resposta contextualiza.

print() #Organizar a apresentação
print("-------------------------------------------------------------------------------------------------") #Organizar a apresentação
print() #Organizar a apresentação

print("Questão 14: Quais são as 10 classificações indicativa de faixa etária da plataforma com mais filmes associados associados?")
print()
# O código movie_df = df[df['type'].str.contains('movie', case=False, na=False)], filtra o dataframe para selecionar apenas produções do tipo 'filme'.
movie_df = df[df['type'].str.contains('Movie',case=False, na=False)]
# O código movie_df['rating'], seleciona a coluna 'rating' do dataframe filtrado para contar apenas valores de filmes.
rating_movie_df = movie_df['rating']
# O código rating_movie_df.str.split(', ') divide as strings da coluna rating_movie_df do Dataframe df, já a função explode() transforma a lista de 'rating', onde cada item da lista irá gerar uma nova linha. 
all_rating_movie = rating_movie_df.str.split(', ').explode()
# O código conta quantas vezes cada classificação de filme aparece na lista all_rating_movie.
rating_movie_counts = all_rating_movie.value_counts()
# O método head() retorna as 10 primeiras linhas de classificações com o maior numero de ocorrência.
top_10_rating_movie = rating_movie_counts.head(10)

print("As top 10 classificações indicativa com mais filmes associados são:")# imprime a resposta contextualiza.
print(top_10_rating_movie)# imprime a resposta contextualiza.

