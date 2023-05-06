ficha = list()
ind = -1

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ind +=1
#ORGANIZANDO A LISTA NO MOMENTO DA CRIAÇÃO!
    ficha.append([ind, nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-='*40)
print('N°.     NOME          MÉDIA')
print('-'*30)

for i in ficha:
    print(f'{i[0]:<5} {i[1]:<5} {i[3]:>15}')
print('-'*30)

#VERIFICAÇÃO DE NOTAS
while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if escolha == 999:
        break
    for i in range(0, len(ficha)):
        if escolha == ficha[i][0]:
            print(f'Notas de {ficha[i][1]} são {ficha[i][2]}')
    print('-'*30)