from random import randint
numeros = (randint(1,50), randint(1,50), randint(1,50), randint(1,50), randint(1,50))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
