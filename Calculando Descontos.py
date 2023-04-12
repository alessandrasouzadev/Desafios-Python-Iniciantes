produto = float (input ('Qual o valor do produto? R$'))

desc = produto - (0.05 * produto)
# desc = produto - (produto * 5 / 100)

print('O valor do produto com o desconto aplicado é de R${:.2f}' .format(desc))
