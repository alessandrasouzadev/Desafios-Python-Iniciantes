'''exe048 calcule a soma entre
todos os numeros impares que são
multiplos de tres e estão entre 1 - 500'''

soma = 0 #ACUMULADOR
cont = 0 #ACUMULADOR
for n in range(1,501,2): #pula 2 casa que contagem será diretamente de ímpares
  if n % 3 == 0:
      cont = cont + 1 #contar os itens ímpares
      soma = soma + n #soma de todos os números ímpares
print('A soma de todos os {} valores solicitados é {}!' .format(cont,soma))
