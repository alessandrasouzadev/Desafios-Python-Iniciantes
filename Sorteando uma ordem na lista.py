import random
a1 = (input('Qual o nome do aluno: '))
a2 = (input('Qual o nome do 2° aluno: '))
a3 = (input('Qual o nome do 3° aluno: '))
a4 = (input('Qual o nome do 4° aluno: '))
todos = [a1,a2,a3,a4]
random.shuffle(todos)
#não há necessidade de se criar outra variavel
print('A ordem de apresentação do trabalho será {}'.format (todos))
