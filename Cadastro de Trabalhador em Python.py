import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
#função para chamar o ano atual
#A função date() na linha 2 retorna um objeto do tipo datetime.date. E este objeto tem year como atributo. Assim, podemos acessá-lo e imprimir o resultado.
cadastro = dict()


for c in range(0,1):
    cadastro['nome'] = str(input('Nome: '))
    anodenasc = int(input('Ano de Nascimento: '))
    cadastro['idade'] = date.year - anodenasc
    cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
    if cadastro['CTPS'] != 0:
        cadastro['contratação'] = int(input('Ano de contratação: '))
        tcont = cadastro['contratação'] + 35
        cadastro['aposentadoria'] = tcont - anodenasc
        cadastro['salario'] = float(input('Salário: R$ '))
print('-'*15)
for k, v in cadastro.items():
    print(f'O {k} tem o valor {v}')
    
