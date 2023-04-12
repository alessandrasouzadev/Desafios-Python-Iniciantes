from random import randint
from time import sleep
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)

#ACUMULADORES
jogador = 0
c = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        print('-'*25)
        print(f'Você jogou {jogador} e o computador {computador}')
        print('-'*25)

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            c +=1
        else:
            print('Você PERDEU!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você PERDEU!')
            c +=1
        else:
            print('Você PERDEU!')
            break

    print('-'*25)
    print('Vamos jogar novamente...')
    sleep(2)
print(f'GAME OVER! Você venceu {c} vezes.')


