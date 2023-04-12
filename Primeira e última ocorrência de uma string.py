#input 'digite uma frase:'
#print 'quantas vezes aparece a letra a?'
#print 'em que posição ela aparece a primeira vez?'
#print 'em que posição ela aparece a última vez?'

frase = str(input('Digite uma frase: '))
print('Quantas vezes aparece a letra a? {}' .format(frase.count('a')))
print('Em que posição aparece a primeira letra a? {}' .format(frase.find('a')))
print('Em que posição aparece a última letra a? {}' .format(frase.rfind('a')))
