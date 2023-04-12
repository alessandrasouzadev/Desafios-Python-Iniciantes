import datetime
print('-='*30)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
ano = int(input('\033[34mDigite seu ano de nascimento:  \033[m'))
print('=-'*30)
atual = datetime.date.today().year
idade = atual - ano
if (atual - ano) <= 9:
    print('O Atleta tem {} anos.' .format(idade))
    print('Classificação: \033[32mMIRIM\033[m')
elif (atual - ano) > 9 and (atual - ano) <= 14:
    print('O Atleta tem {} anos.' .format(idade))
    print('Classificação: \033[32mINFANTIL\033[m')
elif (atual - ano) > 14 and (atual - ano) <= 19:
    print('O Atleta tem {} anos.' .format(idade))
    print('Classificação: \033[32mJUNIOR\033[m')
elif (atual - ano) > 19 and (atual - ano) <= 20:
    print('O Atleta tem {} anos.' .format(idade))
    print('Classificação: \033[32mSÊNIOR\033[m')
else:
    print('O Atleta tem {} anos.' .format(idade))
    print('Classificação \033[32mMASTER\033[m')
