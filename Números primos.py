'''programa que leia um número inteiro e diga se ele é ou não um
'número primo' = divisivel por 1 e por ele mesmo SOMENTE '''

num = int(input('Digite um número: '))
cont = 0
for c in range(1,num+1):
   if num % c == 0:
       cont += 1
       print('\033[33m', end=' ')
   else:
       print('\033[31m', end=' ')
   print('{}' .format(c), end=' ')

print('\033[m\nO número {} foi divisível {} vezes' .format(num,cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
