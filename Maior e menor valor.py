"""leia 3 numeros
print qual é o maior e qual é o menor?"""


a = int(input('Digite um número: '))
b = int(input('Digite o 2° número: '))
c = int(input('Digite o 3° número: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o maior valor digitado foi: {}' .format(maior))
print('o menor valor digitado foi: {}' .format(menor))

