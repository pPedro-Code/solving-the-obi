candidatos = list(map(int, str(input()).split()))
n = candidatos[0]
k = candidatos[1]
notas = list(map(int, str(input()).split()))
notas.sort()
print(notas[-k])
