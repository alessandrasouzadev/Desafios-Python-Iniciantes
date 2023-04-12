''' exe065 leia vários números inteiros
no final da execução mostre a média entre
todos os valores e qual foi o maior e o menor valor
lido
o programa deve perguntar ao usuário se ele 'quer
ou não continuar a digitar valores'
'''

'''contadores'''
media = 0
c = 0
resp = 'S'
maior = 0
menor = 0
total = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    c += 1
    total += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média foi {:.2f}' .format(c,total/c))
print('O maior valor foi {} e o menor foi {}' .format(maior,menor))
