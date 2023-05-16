galera = list()
pessoa = dict()
s, m = 0, 0

#validação de continuação
while True:
    #limpando o dicionário a cada inserção de copia na lista
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    #validação do sexo
    while True:
            pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
            if pessoa['sexo'] in 'MF':
                break;
            print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    s += pessoa['idade']
    galera.append(pessoa.copy())
    #copia de dicionário sendo inserido na lista 

    #validação de dados corretos a continuação
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if r == 'N':
        break

print('-='*30)
print(galera)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
m = s / len(galera)
print(f'B) A média de idade é de {m:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
     if p['sexo'] in 'Ff':
          print(f'{p["nome"]} ', end='')
print()

print(f'D) Lista de pessoas que estão acima da média: ')
for p in galera:
     if p['idade'] >= m:
        print('      ')
        #pesquisa dentro de dicionário, para imprimir chave e valor
        for k, v in p.items():
               print(f'     {k} = {v}; ', end='')
        print()
print('<<<  ENCERRADO   >>>')