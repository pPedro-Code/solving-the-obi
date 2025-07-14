chefe = [] * 100000
n = int(input())
for _ in range(n):
    numero = int(input())
    if numero != 0:
        chefe.append(numero)
    else:
        try:
            chefe.pop()
        except:
            continue
print(sum(chefe))
