'''exe061 refaça o desafio 051
lendo o 'primeiro termo e a razão' de uma PA
mostrando os 10 primeiros termos da progressão aritmetica
'''

c = 0
print('=' *25)
print('Gerador de PA')
print('=' *25)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
while c < 10:
        print(primeiro, end=' → ')
        c += 1
        primeiro += razao
print('ACABOU')
