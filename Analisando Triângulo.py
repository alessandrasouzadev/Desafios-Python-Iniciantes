"""leia o comprimento de 'tres retas '
e diga ao usuario se pode ou não forma um triangulo"""

a = float(input('Qual o comprimento da primeira reta: '))
b = float(input('Qual o comprimento da segunda reta: '))
c = float(input('Qual o comprimento da terceira reta: '))



if a < b + c and b < a + c and c < b + a:
    print('PODE FORMAR um triângulo')
else:
    print('NÃO PODE FORMAR um triângulo')
