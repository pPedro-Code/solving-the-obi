# Definindo as variáveis
l = int(input()) # variável de largura 
c = int(input()) # variável de comprimento
qtd_piso_1 = qtd_piso_2 = 0 # quantidade dos pisos

# Indução do valor da quantidade dos pisos piso 1 e o 2 a partir 
# da análise da imagem do exercício. Respeita as seguintes equações:
qtd_piso_1 = (l * c + (l - 1) * (c - 1))
qtd_piso_2 = (2*(l - 1) + 2*(c - 1))

# Exibindo os valores
print(qtd_piso_1)
print(qtd_piso_2)