alunos = list()
temp = list()
ind = -1

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1+nota2)/2
    ind += 1
    temp.extend([ind,nome, nota1, nota2, media])
    alunos.append(temp[:])
    temp.clear()

    resp = str(input("Quer continuar?  [S/N] "))
    if resp in 'Nn':
        break

print('-='*40)
print('N°.     NOME          MÉDIA')
print('-'*30)

for i in alunos:
    print(f'{i[0]:<5} {i[1]:<5} {i[4]:>15}')
print('-'*30)

while True:
    escolha = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if escolha == 999:
        break
#RETORNO DO DADO PRETENDIDO DENTRO DA LISTA


