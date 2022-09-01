import math
ângulo = float(input('digite o ângulo que voce deseja:'))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem SENO DE {:.2F}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(ângulo, tangente))
