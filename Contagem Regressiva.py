'''exe046 mostrar na tela 'contagem regressiva'
para estouro de fogos de artificio
de 10 até 0, com pausa de 1 segundo entre eles
mostrar emoji de fogos de artificio '''

from time import sleep
for contagem in range (10,0,-1):
    print(contagem)
    sleep(1)
print('FELIZ ANO NOVO! <3')
