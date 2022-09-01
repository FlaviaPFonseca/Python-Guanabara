# crie um programa que leia o quanto de dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# considere US$1.00= R$3,27
real = float(input('Quanto de dinheiro voce tem na carteira? R$ '))
dolar = real / 5.18
print('Com R${:.2f} voce pode comprar  {:.2f} dólares!'.format(real, dolar))


