'''leia 'nome, idade e sexo' 4x pessoas
e no final mostre:
* a média de idade do grupo
* qual é o nome do homem mais velho.
* quantas muheres tem menos de 20 anos '''

media = 0
maior = 0
velho = ''
cont = 0
for c in range (1,5):
    print('----- {}° PESSOA -----' .format(c))
    nome = str(input('Nome: ')).strip()
    Idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += Idade

    if c == 1 and Sexo in 'Mm':
        maior = Idade
        velho = nome
    if Sexo in 'Mm' and Idade > maior:
        maior = Idade
        velho = nome
    elif Sexo in 'Ff' and Idade < 20:
        cont += 1

print('A média de idade do grupo é de {:.2f} anos' .format(media/4))
print('O homem mais velho tem {} anos e se chama {}' .format(maior, velho))
print('Ao todo são {} mulheres com menos de 20 anos' .format(cont))
