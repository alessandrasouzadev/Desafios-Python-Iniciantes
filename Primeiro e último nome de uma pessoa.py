#input 'nome completo'
#print primeiro nome é '...'
#print ultimo nome é'...'

nome = str(input('Qual o seu nome completo? '))
dividir = nome.split()
print('Primeiro nome: {}' .format(dividir[0]))
print('Último nome: {} ' .format(dividir[-1]))
