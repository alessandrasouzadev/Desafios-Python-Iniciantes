'''
exe049 REFAÇA O DESAFIO 009 TABUADA
com o número que o usuário escolher e utilize o laço for'''

for tabuada in range(0,1):
    n = int(input('Digite um número: '))
    print('A tabuada do número {} é a seguinte!' .format(n))
print('\033[31m*\033[m' * 15)
for n1 in range (0,11):
    print('{} x {} = {}'.format(n,n1, n * n1))
print('\033[31m*\033[m' * 15)

