from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(0,6),
        'Jogador2': randint(0,6),
        'Jogador3': randint(0,6),
        'Jogador4': randint(0,6),
        }
ranking = dict()

print('Valores sorteados: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

print('-='*15)
print(' == RANKING SORTEADO == ')

#a chave foi listada como (1) para ordenar a partir do resultado que está na posição (1) || e quando listamos em ordem crescente, ele automatica se torna uma lista, ou seja o enumarete está abaixo por essa lógica
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)



