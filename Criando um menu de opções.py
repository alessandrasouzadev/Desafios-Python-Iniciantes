'''exe059 criar um programa que digite
2 números e mostre um MENU
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa '''

from time import sleep
maior = 0
opcao = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opcao != 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior')
    print('[ 4 ] novos números\n[ 5 ] sair do programa')
    opcao = int(input('>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1+n2
        print('A soma entre {} + {} é {}' .format(n1,n2,soma))
        sleep(2)
    elif opcao == 2:
        produto = n1*n2
        print('O Resultado de {} x {} é {}' .format(n1,n2,produto))
        sleep(2)
    elif opcao == 3:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
                print('Entre {} e {} o maior valor é {}' .format(n1,n2,maior))
                sleep(2)
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        sleep(2)
    elif opcao == 5:
        print('Finalizando...')
        sleep(3)
    else:
        print('Opção inválida. Tente novamente')
        sleep(3)
    print('=-' * 15)
print('Fim do programa! Volte sempre!')
