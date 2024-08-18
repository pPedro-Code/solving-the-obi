verificador = [False] * 10
contador = [0] * 10

while True:
    c = 0
    lugar = int(input('posição: '))
    forma = int(input('ligado/desligado: '))
    if forma == 1:
        verificador[lugar] = True
    elif forma == 0:
        verificador[lugar] = False
    for teste in verificador:
        if teste:
            contador[c] += 1
        c += 1
    print(verificador)
    print(contador)
