casa = float(input('Qual o valor da casa que deseja comprar? R$'))
salario = float(input('Qual o salário do comprador? R$'))
ano = int(input('Em quantos anos pretende pagar? '))
excedente = salario * 0.30
parcela = casa/(ano * 12)
if parcela > excedente:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} \nEmpréstimo NEGADO!' .format(casa,ano,parcela))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}\nEmpréstimo AUTORIZADO!' .format(casa,ano,parcela))
