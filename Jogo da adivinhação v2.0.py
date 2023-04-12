'''exe058 melhorar o jogo do desafio 28
o computador vai pensar em um número entre 0 e 10
o jogador vai tentar adivinhar até acertar
mostrando no final quantos palpites foram necessários
para vencer '''

from random import randint
palpite = randint(0,10)
usuario = 0
tentativa = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi? ')
while usuario != palpite:
    usuario = int(input('Qual é o seu palpite? '))
    if usuario != palpite:
        if usuario < palpite:
            print('Mais... Tente mais uma vez.')
            tentativa += 1
        else:
            print('Menos... Tente mais uma vez.')
            tentativa += 1
print('Acertou com {} tentativas. Parabéns' .format(tentativa+1))
