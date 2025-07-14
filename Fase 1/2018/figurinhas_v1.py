# Definindo variáveis
repetidas = [] # lista de valores já lidos (detalhes mais para frente)
album = str(input()).split() # detalhes do álbum de figurinha:
n = int(album[0])   # quantidade total de figurinhas no álbum
c = int(album[1])   # quantidade total de figurinhas carimbadas no álbum
m = int(album[-1])  # quantidade de figurinhas que possui

carimbdas_figurinhas = str(input()).strip().split() # número das figurinhas carimbadas
compradas_figurinhas = str(input()).strip().split() # número das figurinhas que possui

contador = 0 # contador de figurinhas que possui

# iteração entre o número das figurinhas que possui e as carimbadas
for indice in compradas_figurinhas:
    # Se forem iguais e não for repetido, então contador aumenta um
    if indice in carimbdas_figurinhas and indice not in repetidas:
        contador += 1
    # Após o valor ser comparado, é guardado, para não conta-lo mais de uma vez
    repetidas.append(indice)

# Exibindo a diferença da quantidade que possui daquilo que se tem, ou seja, quantas faltam
print(len(carimbdas_figurinhas) - contador)