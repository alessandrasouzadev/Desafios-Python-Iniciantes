'''exe063 leia 'numero n inteiro
' e mostre na tela os 'n primeiros
elementos de uma sequencia fibonacci'

ex: 0 → 1 → 1 → 2 → 3 → 5 → 8'''


n = 0
print('-'*15)
print('Sequência de Fibonacci')
print('-'*15)
n = int(input('Quantos termos você quer mostrar? '))
c = 0
t1 = 0
t2 = 1
print('~~'*20)
print('{} → {}' .format(t1,t2), end='')
cont = 3
while c <= n:
    t3 = t1 + t2
    print(' → {}' .format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' → FIM')
