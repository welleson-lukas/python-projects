"""
PROGRAMA QUE LE UM ANGULO QUALQUER E MOSTRA O VALOR DO SENO, COSSENO
E TANGENTE DESSE ANGULO
"""
import math
an = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, tangente))