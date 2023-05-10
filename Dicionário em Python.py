aluno = dict()

for c in range(0,1):
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
    if aluno['media'] >= 7:
        aluno['situação'] = 'Aprovado'
    elif aluno['media'] < 7:
        aluno['situação'] = 'Recuperação'
    else:
        aluno['situação'] = 'Reprovado'
print('-'*20)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
