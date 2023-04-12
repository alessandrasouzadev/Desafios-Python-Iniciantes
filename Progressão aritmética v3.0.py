'''exe062 melhorar o desafio 61
vai continuar amostrando os
10 primeiros termos
porém ele vai perguntar ao usuario
'se ele quer mostrar mais alguns termos'
o programa encerra quando ele mostrar
que quer '0 termos'''

from time import sleep
c = 0
mais = 0
primeiro = 0
print('=' * 25)
print('Gerador de PA')
print('=' * 25)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.' .format(total))


