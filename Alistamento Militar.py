import datetime
ano = int(input('Qual seu ano de nascimento? '))
atual = datetime.date.today().year
#periodo = (atual - ano) - 18
if atual - ano < 18:
    print('Quem nasceu em {} tem {} anos em {}.' .format(ano, atual - ano, atual))
    print('Ainda faltam {} anos para o alistamento'.format(18 - (atual - ano)))
    print('Seu alistamento será em {}' .format(18 - (atual - ano) + atual))
elif atual - ano == 18:
    print('Quem nasceu em {} tem {} anos em {}' .format(ano, atual - ano, atual))
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Quem nasceu em {} tem {} anos em {}' .format(ano, atual - ano, atual))
    print('Já se passaram {} anos para o alistamento'.format((atual - ano) - 18))
    print('Deveria ter se alistado no ano de {}' .format(18 - (atual - ano) + atual))



