vacuo = [False] * 100
amigo = [0] * 100

n = int(input())
for _ in range(n):
    c = 0
    forma, numera = input().split()
    numera = int(numera)
    if forma == 'R':
        vacuo[numera] = True
    elif forma == 'E':
        vacuo[numera] = False
    elif forma == 'T':
        for teste in vacuo:
            if teste:
                amigo[c] += numera
            c += 1
    if forma != 'T':
        for teste in vacuo:
            if teste:
                amigo[c] += 1
            c += 1
c = 0

for lugar in amigo:
    c += 1
    if lugar != 0 and not vacuo[c]:
        print(c-1, lugar-1)
    elif lugar != 0 and vacuo[c]:
        print(c-1, -1)
