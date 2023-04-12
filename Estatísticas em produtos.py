print('-'*25)
print('LOJA SUPER BARATÃO')
print('-'*25)
produto = ' '
valor = 0
soma = contproduto = menor = c = 0
barato = ''

while True:
    produto = str(input('Nome do Produto: ')).strip()
    valor = float(input('Preço: R$'))
    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        c += 1
        soma += valor
    if valor > 1000:
        contproduto += 1
    if c == 1 or valor < menor: #simplificação
        menor = valor
        barato = produto #o nome do produto vai acompanhar o valor

    if continuar == 'N':
        print('-------- FIM DO PROGRAMA ----------')
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {contproduto} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
