'''exe064 leia vários números inteiros
o programa só vai parar quando o usuário digitar o
valor 999 (condição de parada)
no final, mostre quantos números foram digitados
e qual foi a soma entre eles
desconsiderando o 999 (flag)'''

n = 0
s = 0
c = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        s += n
        c += 1
print('Você digitou {} números e a soma entre eles foi {}.' .format(c,s))
