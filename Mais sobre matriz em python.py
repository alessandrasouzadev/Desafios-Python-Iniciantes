matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = scol = mai = 0

#inserção
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)

#organização
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

#verificação
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é de {par}.')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz [1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maio valor da segunda linha é {mai}')