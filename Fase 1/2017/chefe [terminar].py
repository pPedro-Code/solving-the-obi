# Atribuindo valores
empregados, relacoes_direta, instrucoes = list(map(int, str(input()).strip().split()))
idades_empregados = list(map(int, str(input()).strip().split()))
relacoes = []
historico = []
for _ in range(empregados):
    relacoes.append([])

for _ in range(relacoes_direta):
    gerenciador, gerenciado = list(map(int, str(input()).strip().split()))
    relacoes[gerenciador - 1].append(gerenciado)

for _ in range(instrucoes):
    instrucao = str(input()).strip().split()
    identificador = instrucao[0]

    if identificador == 'T':
        empregado_atual, empregado_substitutor = list(map(int, (instrucao[1], instrucao[2])))
        empregado_atual = empregado_atual -1
        empregado_substitutor = empregado_substitutor -1
        relacoes_antigas = relacoes[empregado_atual][:], relacoes[empregado_substitutor][:]
        relacoes[empregado_atual] = relacoes_antigas[1]
        relacoes[empregado_substitutor] = relacoes_antigas[0]

    if identificador == 'P':
        mais_novo = 0
        chamado = int(instrucao[1])
        contador = 0
        for pessoa in relacoes:
            if chamado in pessoa:
                if mais_novo == 0:
                    mais_novo = idades_empregados[contador]
                elif idades_empregados[contador] < mais_novo:
                    mais_novo = idades_empregados[contador]
            contador += 1
        if mais_novo == 0:
            mais_novo = '*'
        historico.append(mais_novo)

for pesquisa in historico:
    print(pesquisa)