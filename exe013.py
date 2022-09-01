# faça um algoritmo que leia o salário de um funcionário e
# mostre o novo salário com 15% de aumento.
sal = float(input('Qual o salario do funcionário? R$'))
novo = sal +(sal * 15 / 100)
print(' O salário do funcionario que ganhava R$ {:.2f} com 15% de aumento passará a ganhar R${:.2f}'.format(sal, novo))
