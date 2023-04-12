import random
alun1 = str(input('Digite o nome do aluno: '))
alun2 = str(input('Digite o nome do 2° aluno: '))
alun3 = str(input('Digite o nome do 3° aluno: '))
alun4 = str(input('Digite o nome do 4° aluno: '))
lista = [alun1,alun2,alun3,alun4]
#AS LISTAS SÃO FORMADAS POR COLCHETES []
escolhido= random.choice(lista)
print('O aluno sorteado foi: {}' .format(escolhido))

#metodo 'choice' da biblioteca 'random'
