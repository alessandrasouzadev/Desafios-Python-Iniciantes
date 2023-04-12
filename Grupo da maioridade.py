'''leia ano de nascimento de 7 pessoas
no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

MAIOR IDADE = 21'''
import datetime
maior = 0
menor = 0
atual = datetime.date.today().year
for c in range (1,8):
    ano=int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    if atual - ano >= 21:
        maior += 1
    else:
        menor +=1
print('Ao todo tivemos {} pessoas maiores de idade' .format(maior))
print('E também tivemos {} pessoas menores de idade' .format(menor))
