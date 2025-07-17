n, k = list(map(int, (input().strip().split())))
retangulo = list(map(int, (input().strip().split())))

contador = 0
for x in range(n):
    y = x
    while y < n:
        y += 1
        if sum(retangulo[x:y]) == k:
            contador += 1
print(contador)