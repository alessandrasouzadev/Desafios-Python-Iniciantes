'''leia uma 'frase qualquer'
e diga se é um 'palíndromo, desconsiderando os espaços

-> palavras que são iguais de frente pra trás e de trás pra frente'''

frase = str(input('Digite uma frase: ')).strip().upper()
separa = frase.split()
junto = ''.join(separa)
inverso =''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('NÃO temos um palíndromo!')

'''OU PODERIA FAZER A TECNICA DE FATIAMENTO 
inverso = junto[::-1]
não teria necessidade de utilizar o 'FOR' '''
