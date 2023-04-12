num = list()
par = list()
impar = list()

while True:
    n = int(input('Digite um número: '))
    num.append(n)
    r = str(input('Quer continuar? [S/N] '))
    if r in "Nn":
        break
for i in range(len(num)):
    if num[i] % 2 == 0:
        par.append(num[i])
    else:
        impar.append(num[i])

print('-='*20)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
