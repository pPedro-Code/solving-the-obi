idade_monica = int(input())
idade_filho_1 = int(input())
idade_filho_2 = int(input())
idade_filho_3 = idade_monica - (idade_filho_2 + idade_filho_1)
idade_filhos = idade_filho_2, idade_filho_1, idade_filho_3
print(max(idade_filhos))