num = list()
for c in range(0,5):
    dado = int(input('Digite um número: '))
    if c == 0 or dado > dado[-1]:
        num.append(dado)
        print('Adicionado ao final da lista...')
      
    else:
        #Verificação de posição - percorrer o vetor para inserção de dados.
        pos = 0
        while pos < len(num):
            if dado <= num[pos]:
                num.insert(pos, dado)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {num}')
