# lista pessoas
#dicionario = dados individuais (nome, sexo, idade)

pessoas = list()
dados = dict()
s, m = 0, 0


while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: '))
    dados['idade'] = int(input('Idade: '))
    s += dados['idade']
    pessoas.append(dados.copy())
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break 

for k,v in dados.items():
    print(f'{k} tirou {v} no dado.')
#VOU TER QUE COLOCAR UM FOR DENTRO DO WHILE TRUE

print(m)
print(pessoas)
print(s)
