#Faça um programa que leia a altura e a largura de uma parede
# em metros e calcule a area e a quantidade de tinta necessária para pintala.
# Sabe se que cada litro de tinta pinta uma area de 2 m².
larg = float(input('largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem dimensões de {}x{} e sua área é de {}m² de tinta'.format(larg, alt, área))
tinta = área / 2
print('Para pintar esta parede de {}m², voce precisará de {} de tinta'.format(área, tinta))

