# escreva um programa que leia o valor em metro e
# exiba convertido em centímetros e milímetros
medida = float(input('Informe uma distância em metros:'))
km = medida / 1000
cm = medida * 100
mm = medida * 1000
print(' O valor de medida {} em km é:{}km \n em cm é: {}cm \n o valor em mm é:{}mm'.format(medida, km, cm, mm))
