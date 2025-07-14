# Subterafa A:
cheques = []

# 
linha_um = list(map(int, str(input()).strip().split()))
m = linha_um[0]  # número de cheques emitidos
n = linha_um[-1] # número de habitantes da cidade

for _ in range(m):
    cheques.append(list(map(int, str(input()).strip().split())))
print(cheques)