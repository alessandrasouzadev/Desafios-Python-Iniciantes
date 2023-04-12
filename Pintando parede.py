larg = float( input ('Quantos metros de largura possui sua parede? '))
alt = float (input ('Quantos metros de altura possui a sua parede? '))

area = larg * alt
tinta = area/2


print('Sua parede tem a dimensão de {}x{} e sua area é de {:.4}m3². ' .format(larg,alt,area))
print ('É necessário {:.4} litros de tinta para pinta-lá' .format(tinta))



