n = int(input('Digite um número qualquer: '))
print('-=' *30)
print('''Escolha uma das bases para conversão:
[ 1 ] = Binário
[ 2 ] = Octal
[ 3 ] = Hexadecimal''')
print('-=' *30)
opção = int(input('Qual será a base de conversão: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}' .format(n, bin(n)[2:])) # modulo de bases
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}' .format(n, oct(n)[2:])) #principio de fatiamento
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}' .format(n, hex(n)[2:]))
else:
    print('DADO INVÁLIDO!')

'''if conversão == 1:
    conversão = dado % 2
    print(dado)
else:
    print('ok')'''
