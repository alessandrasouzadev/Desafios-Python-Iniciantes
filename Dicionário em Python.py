aluno = dict()

for c in range(0,1):
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input(f'Média de {aluno["nome"]}'))
    if aluno['media'] > 7:
        aluno['situação'] = 'Aprovado'
    else:
        aluno['situação'] = 'Reprovado'
print(f'Nome é igual a {aluno["nome"]}\nMédia é igual a {aluno["media"]}\nSituação é igual a {aluno["situação"]}')
