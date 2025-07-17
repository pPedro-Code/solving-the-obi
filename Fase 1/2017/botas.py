# Lista de pares e quantidade
bota_esquerda = {}
bota_direita = {}

# Quantidade de botas
n = int(input().strip())

# Adiconando e contando as botas
for _ in range(n):
    l = input().strip().split()
    if l[1] == 'E':
        if l[0] in bota_esquerda:
            qtd_botas = bota_esquerda.get(l[0]) + 1
        else:
            qtd_botas = 1
        bota_esquerda[l[0]] = qtd_botas

    if l[1] == 'D':
        if l[0] in bota_direita:
            qtd_botas = bota_direita.get(l[0]) + 1
        else:
            qtd_botas = 1
        bota_direita[l[0]] = qtd_botas

# Contando pares possíveis
pares = 0
for tamanho_esquerda, quantidade_esquerda in bota_esquerda.items():
    for tamanho_direita, quantidade_direita in bota_direita.items():
        if tamanho_esquerda == tamanho_direita:
            # Separar o maior do menor valor
            quantidade_botas = [quantidade_esquerda, quantidade_direita]
            pares += min(quantidade_botas)

print(pares)