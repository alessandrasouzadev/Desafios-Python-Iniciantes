catoposto = float(input ('Qual o comprimento do Cateto Oposto? '))
catadjacente = float (input('Qual o comprimento do cateto adjacente? '))
from math import hypot
hipo = hypot(catoposto,catadjacente)
print('O comprimento da hipotenusa é: {:.2f}' .format(hipo))
