print('*' *30)
print('\033[32mCALCULE O SEU IMC\033[m')
print('*' *30)
nome = str(input('Qual o seu nome: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso/(altura ** 2)
print('O seu IMC é de {:.1f}' .format(imc))

if imc < 18.5:
    print('{} você está \033[32mABAIXO DO PESO\033[m' .format(nome))
elif  18.5 <= imc < 25:
    print('{} você está em um \033[32mPESO NORMAL\033[m' .format(nome))
elif 25 <= imc < 30:
    print('{} você está em \033[32mSOBREPESO\033[m' .format(nome))
elif 30 <= imc < 40:
    print('{} você está \033[32mOBESIDADE\033[m' .format(nome))
else:
    print('{} você está em \033[32mOBESIDADE MÓRBIDA\033[m' . format(nome))
