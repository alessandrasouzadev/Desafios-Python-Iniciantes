'''exe057 ler o sexo da pessoa
mas só aceite os valores 'M' ou 'F'
caso contrario peça a digitação novamente
até o valor correto'''

sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0] #só pegará a primeira letra
while sexo not in 'MmfF':
    sexo = str(input('Dados Inválidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso' .format(sexo))


'''Validação de Dados '''
