print('='* 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))

total = valor #montante
céd = 50 #cedula máxima
totcéd = 0 #total da contagem

while True:
    if total >= céd: #contagem se inica com 50
        total -= céd
        totcéd += 1
    else: #se não iniciada por 50, percorre:
        if totcéd > 0:
            print(f'Total de {totcéd} de R${céd}') #se o total foi >0 ele será impresso
        if céd == 50: #identificação para a cédula atual
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break

print('='*20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
