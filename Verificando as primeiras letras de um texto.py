#input 'sua cidade'
#input sua cidade COMEÇA ou não com nome 'santo'

cidade = str(input('Qual o nome da sua cidade? '))
dividir = cidade.split()
inicio = dividir[0]
verificar = 'Santo' in inicio
print('Sua cidade começa ou não com a palavra santo? {}' .format(verificar))
