#exe022 LER O NOME COMPLETO DA PESSOA
#PRINT - NOME COM TODAS AS LETRAS MAIUSCULAS
#PRINT - NOME COM TODAS AS LETRAS MINUSCULA
#PRINT - QUANTAS LETRAS AO TODO (SEM ESPAÇO)
#PRINT - QUANTAS LETRAS TEM O 'PRIMEIRO NOME'

nome = str(input(('Qual o seu nome completo? ')))
nomelista = nome.split()
nomediv = len(nomelista[0])
print('O seu nome com todas as letras maiúsculas ficaria: {}' .format(nome.upper()))
print('O seu nome com todas as letras minúsculas ficaria: {}' .format(nome.lower()))
print('A quantidade de letras que obtém o seu nome é de: {}'  .format(len(nome.replace(' ',''))))
print('A Quantidade de letras que obtém o primeiro nome é de: {}' .format(nomediv))
