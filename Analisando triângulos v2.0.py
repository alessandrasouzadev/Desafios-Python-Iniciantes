print('*' * 30)
print('\033[35mDESCUBRA QUAL É O TIPO DO TRIÂNGULO\033[m')
print('*' * 30)
a = float(input('\033[34mQual o comprimento da primeira reta: '))
b = float(input('Qual o comprimento da segunda reta: '))
c = float(input('Qual o comprimento da terceira reta: \033[m'))
'''triangulo = a < b + c and b < a + c and c < b + a

if triangulo and a == b == c:
    print('E O triângulo formado é um \033[36mEQUILÁTERO\033[m')
elif triangulo and a == b or b == c or c == a:
    print('E O triângulo formado é um \033[36mISÓSCELES\033[m')
elif triangulo and a != b != c != a:
    print('E O triângulo formado é um \033[36mESCALENO\033[m')
else:
    print('\033[36mNÃO\033[m é possível formar um triângulo')'''

#TAMBÉM EXISTE A POSSIBILIDADE DE COLOCAR UM IF DENTRO DE OUTRO

if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima PODEM FORMAR um triângulo')
    if a == b == c:
        print('EQUILÁTERO')
    if a != b != c != a:
        print('ESCALENO') #CONDIÇÕES ANINHADAS
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulos')
