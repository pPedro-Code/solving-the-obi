# Definindo variáveis
album = str(input()).split() # detalhes do álbum de figurinha:
n = int(album[0])   # quantidade total de figurinhas no álbum
c = int(album[1])   # quantidade total de figurinhas carimbadas no álbum
m = int(album[-1])  # quantidade de figurinhas que possui

carimbdas_figurinhas = str(input()).strip().split() # número das figurinhas carimbadas

# número das figurinhas que possui -> set para não ter fig. repetida
compradas_figurinhas = set(str(input()).strip().split())

contador = 0 # contador de figurinhas que possui

# iteração entre o número das figurinhas que possui e as carimbadas
for indice in compradas_figurinhas:
    # Se forem iguais e não for repetido, então contador aumenta um
    if indice in carimbdas_figurinhas:
        contador += 1

# Exibindo a diferença da quantidade que possui daquilo que se tem, ou seja, quantas faltam
print(len(carimbdas_figurinhas) - contador)