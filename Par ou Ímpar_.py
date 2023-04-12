"""input numero inteiro
mostre na tela se é impar ou par"""

num = int(input('\033[35mMe diga um número qualquer: \033[m'))
resto = num % 2

if resto == 0:
    print('O número {} é \033[34mPAR'.format(num))
else:
    print('O número {} é \033[34mÍMPAR' .format(num))
