"""input velocidade de um carro
se ultrapassar 80km/h (mostre mensagem dizendo que ele foi multado por R${})
a multa vai custar 7,00 para cada km acima do limite"""

vel = float(input('Qual a velocidade do seu carro? '))
multa = (vel-80) * 7
if vel > 80.0:
    print('\033[31mMULTADO! Você excedeu o limite permitido queé de 80Km/h')
    print('\033[31mVocê deve pagar uma multa de R${}' .format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
