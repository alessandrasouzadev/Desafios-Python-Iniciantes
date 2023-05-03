indice = []
nome = []
notas = []
media = []
alunos = [indice,nome,notas,media]
ind = -1

while True:

    name = str(input('Nome: '))
    nome.append(name)

    one = float(input('Nota 1: '))
    notas.append(one)
    two = float(input('Nota 2: '))
    notas.append(two)

    res = one + two/2
    media.append(res)

    ind += 1
    indice.append(ind)

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 40)
print('N°.   NOME              MÉDIA')
print('-'*30)

for i in indice:
    print(f'{indice[i]: <5} {nome[i]: <10} {media[i]: >10}')





