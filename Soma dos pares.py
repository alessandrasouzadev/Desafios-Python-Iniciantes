'''exe050 programa que leia 6 números inteiros
e mostre a soma APENAS DAQUELES QUE FOREM PARES
se o valor for IMPAR (desconsidere)'''

soma = 0
cont = 0
for n in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print('Você informou {} números PARES e a soma foi {}' .format(cont,soma))


