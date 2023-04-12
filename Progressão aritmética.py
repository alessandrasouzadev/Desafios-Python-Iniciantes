'''ler um 'primeiro termo' e a 'razão' de uma PA (progressão aritmética)
no final, mostre os 10 primeiros termos dessa progressão'''

print('=' *25)
print('10 TERMOS DE UMA PA')
print('=' *25)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range(1,11):
    print(primeiro, end='→ ')
    if c < 10:
        primeiro += razao
print('ACABOU')
