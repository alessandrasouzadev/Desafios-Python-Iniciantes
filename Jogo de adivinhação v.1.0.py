"""escrever um programa que faça o pc 'pensar' em um numero inteiro (0 a 5)
e peça para o usuario tentar descobrir qual foi o escolhido
programa deverá escrever na tele se o usuario 'venceu ou perdeu'"""


from random import randint
from time import sleep #MODULO de tempo para simular um processamento do sistema
pensar = randint(0,5)
print('\033[33m-='*30)
print('\033[1;34mVou pensar em um número entra 0 e 5. Tente adivinhar...')
print('\033[33m-=\033[m'*30)
usuario = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...') #crie a palavra que ficará em processamento
sleep(3) #defina o periodo de segundos que ficará disponivel até aparecer a próxima resposta
if usuario == pensar:
    print('\033[32mPARABENS! Você conseguiu me vencer!')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}!' .format(pensar,usuario))


