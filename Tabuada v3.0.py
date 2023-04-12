
while True:
    print('-' * 20)
    n = int(input('Quer ver a tabuada de qua valor? '))
    print('-' * 20)
    if n < 0:
        break
    for n1 in range(0,11):
        print(f'{n} x {n1} = {n*n1}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
