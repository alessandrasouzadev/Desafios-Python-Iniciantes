desempenho = dict()
gols = list()
t = 0


desempenho['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {desempenho["nome"]} jogou? '))
for i in range(0,partidas):
    gols.append(int(input(f'       Quantos gols na partida {i+1}? ')))
    t = t + gols[i]
desempenho['gols'] = gols
desempenho['total'] = t
print('-'*30)
print(desempenho)
print('-'*30)

for k, v in desempenho.items():
    print(f'O campo {k} tem o valor {v}.')
print('-'*30)

print(f'O jogador {desempenho["nome"]} jogou {partidas} partidas.')
for i in range(0,len(desempenho["gols"])):
    print(f'       => Na partida {i+1}, fez {desempenho["gols"][i]} gols.')

print(f'Foi um total de {desempenho["total"]} gols.')
