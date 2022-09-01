dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km percorridos pelo carro? '))
pago = (dias * 60) + (km * 0.15)
print(' o total a pagar é de R${:.2f}'.format(pago))
