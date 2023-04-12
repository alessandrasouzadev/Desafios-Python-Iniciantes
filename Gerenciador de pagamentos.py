print('{:=^40}' .format(' LOJAS GUANABARA '))
produto = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque \n[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão')
pg = int(input('Qual é a opção? '))

if pg == 1:
    print('Sua compra de R${} vai custar R${:.2f} com 10% de desconto' .format(produto, produto - (produto * 0.10)))
elif pg == 2:
    print('Sua compra de R${} vai custar R${:.2f} com 5% de desconto' .format(produto,produto - (produto * 0.05)))
elif pg == 3:
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(2,produto/2))
    print('Sendo o seu valor integral de R${:.2f}' .format(produto))
elif pg == 4:
    parcela = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS' .format(parcela, (produto+(produto * 0.20))/parcela))
    print('Sua compra de R${:.2f} vai custar R${} com 20% de juros' .format(produto, produto + (produto * 0.20)))
else:
    print('DADO INVÁLIDO!')
