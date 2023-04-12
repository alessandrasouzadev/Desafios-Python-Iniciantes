'''exe060 programa ler um número qualquer e
mostrar um fatorial
ex: 5! = 5x4x3x2x1 = 120'''


n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c),end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}' .format(f))
