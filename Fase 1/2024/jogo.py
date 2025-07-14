matriz = []
eixo_x = eixo_y = pos_x = pos_y = 0

detalhes_matriz = list(map(int, str(input()).split()))
n = detalhes_matriz[0]
q = detalhes_matriz[1]

for _ in range(n):
    matriz.append(str(input()))

def vivo_morto(estado_vida, qtd_vivo):
    # 1 vivo - 0 morto
    estado_vida = int(estado_vida)
    if estado_vida == 0 and qtd_vivo == 3:
        return 1
    elif estado_vida == 0 and qtd_vivo != 3:
        return 0
    elif estado_vida == 1 and (2 == qtd_vivo or qtd_vivo== 3):
        return 1
    elif estado_vida == 1 and qtd_vivo < 2:
        return 0
    else:
        return 0

for _ in range(q):
    while eixo_x != n:
        contador_1 = 0
        for x in range(-1, 2):
            pos_x = eixo_x + x
            for y in range(-1, 2):
                pos_y = eixo_y + y
                # erro aqui
                if (0 <= pos_x < n and 0 <= pos_y < n) and not (x == 0 and y == 0):
                    if int(matriz[pos_x][pos_y]) == 1:
                        contador_1 += 1
        # erro aqui
        matriz.pop([eixo_x][eixo_y])
        matriz.insert([eixo_x][eixo_y], str(vivo_morto(matriz[eixo_x][eixo_y], contador_1)))
        eixo_y += 1
        eixo_x += 1

for x in range(n):
    for y in range(n):
        print(matriz[x][y])
    print('\n')