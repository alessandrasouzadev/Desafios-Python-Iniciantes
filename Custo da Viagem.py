"""pergunte a distancia de uma viagem em km
calcule o preço da passagem, cobrando 0.50 por km para viagem de até 200km
e 0.45 para viagens mais longas"""

dist = float(input('Qual a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(dist))
if dist <= 200:
    print('E o preço da sua passagem será de R${:.2f}' .format(0.50*dist))
else:
    print('E o preço da sua passagem será de R${:.2f}' .format(0.45*dist))

'''preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45'''
