import random
from time import sleep #MODULO de tempo para simular um processamento do sistema


print('\033[35m*'*30)
print('\033[1;34mVamos jogar JOKENPÔ?\033[m')
usuario = int(input('''Suas Opções: 
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
print('\033[35m*\033[m'*30)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2)



print('\033[37mJO') #crie a palavra que ficará em processamento
sleep(1)#defina o periodo de segundos que ficará disponivel até aparecer a próxima resposta
print('KEN')
sleep(1)
print('PO!!!\033[m')
sleep(1)

print('-=' * 15)
print('O computador escolheu {}' .format(itens[computador]))
print('O Jogador escolheu {}' .format(itens[usuario]))
print('-=' * 15)

if computador == 0:
   if usuario == 0: #Computador jogou PEDRA
       print('EMPATAMOS')
   elif usuario == 1:
        print('JOGADOR VENCEU')
   elif usuario == 2:
       print('COMPUTADOR VENCEU')
   else:
       print('JOGADA INVÁLIDA!')
elif computador == 1: #computador jogou PAPEL
    if usuario == 0:
        print('COMPUTADOR VENCEU')
    elif usuario == 1:
        print('EMPATAMOS')
    elif usuario == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #computador jogou TESOURA
    if usuario == 0:
        print('JOGADOR VENCEU')
    elif usuario == 1:
        print('COMPUTADOR VENCEU')
    elif usuario == 2:
        print('EMPATAMOS')
    else:
        print('JOGADA INVÁLIDA!')



