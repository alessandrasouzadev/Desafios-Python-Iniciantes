"""input salario
calcule o valor do aumento
para salarios superiores a R$1.250 calcule 10%
para salarios inferiores calcular 15%"""

salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250:
    novo = salario + (0.15 * salario)
else:
    novo = salario + (0.10 * salario)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora' .format(salario,novo))
