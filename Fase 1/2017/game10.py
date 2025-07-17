posicoes = int(input())
disco_voador = int(input())
nave = int(input())

apertadas = 0
for _ in range(posicoes):
    if nave == disco_voador:
        break
    apertadas += 1

    # Limitar a nave dentro do número possível de posições
    if nave < posicoes:
        nave += 1
    else:
        nave = 1

print(apertadas)