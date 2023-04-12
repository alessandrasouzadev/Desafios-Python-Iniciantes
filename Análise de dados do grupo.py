#ACUMULADORES|CONTADORES
idade = 0
sexo = ' '
maior18 = 0
cadastrohomem = 1
mulher20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-'*20)
    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'S':
        if idade > 18:
            maior18 += 1
        if sexo == 'M':
            cadastrohomem += 1
        if idade < 20 and sexo == 'F':
            mulher20 += 1
    elif continuar == 'N':
        print('===== FIM DO PROGRAMA ======')
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}.')
print(f'Ao todo temos {cadastrohomem} homens cadastrados.')
print(f'E temos {mulher20} mulheres com menos de 20 anos.')

