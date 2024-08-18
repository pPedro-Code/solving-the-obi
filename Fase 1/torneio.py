# Declaração das variáveis
vitorias = g = 0

# Loop tipo for que não contará/guardará uma variável para as repetições
for _ in range(0, 6):
    resultado = str(input()).lower()
    if resultado == 'v':
        vitorias += 1
if vitorias >= 5:
    grupo = 1
elif vitorias >= 3:
    grupo = 2
elif vitorias >= 1:
    grupo = 3
else:
    grupo = -1
print(grupo)
