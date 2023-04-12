valores = list()

while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
    if r in 'Nn':
        break
        
print('-='*30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista')
