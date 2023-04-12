#input numero de 0 ate 9999 'Digite um numero: ex 1834'
#print unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

num = (input('Digite um número entre 0 e 9999: '))
print('Unidade: {}' .format(num[3]))
print('Dezena: {}' .format(num[2]))
print('Centena: {}' .format(num[1]))
print('Milhar: {}' .format(num[0]))
