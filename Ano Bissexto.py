"""input digite um ano?
e mostre se ele é um ano BISSEXTO OU NÃO"""

from datetime import date # modulo de importações de datas(ano,mes,dia)
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: ')) # ano bissexto é todo aquele divisivel por 4
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #o ano NÃO é BISSEXTO se divisivel por 100, mas não 400
    print('O ano {} é BISSEXTO' .format(ano))
else:
    print('O ano {} NÃO é BISSEXTO' .format(ano))

