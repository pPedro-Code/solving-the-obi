def consoante(x):
    g = c = 0
    tras = frente = ''
    lugar = alfabeto.index(x)
    for letra in alfabeto[lugar::-1]:
        g += 1
        if letra in vogais:
            tras = letra
            break
    for letra in alfabeto[lugar:]:
        if letra == 'z':
            c = 999
        c += 1
        if letra in vogais:
            frente = letra
            break
    if c >= g:
        return tras
    else:
        return frente


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
vogais = ['a', 'e', 'i', 'o', 'u']
palavra = str(input()).lower()
cifra = [] * 30
for letraP in palavra:
    cifra.append(letraP)
    if letraP not in vogais:
        cifra.append(consoante(letraP))
        if letraP != 'z':
            if alfabeto[alfabeto.index(letraP) + 1] not in vogais:
                cifra.append(alfabeto[alfabeto.index(letraP) + 1])
            else:
                cifra.append(alfabeto[alfabeto.index(letraP) + 2])
        elif letraP == 'z':
            cifra.append('z')
for finalmente in cifra:
    print(finalmente, end='')
