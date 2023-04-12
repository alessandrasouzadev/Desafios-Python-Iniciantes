núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'você digitou os valores {núm}')
print(f'o valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os números pares digitados foram ', end=' ')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')

