"""
LEIA UM NUMERO REAL E MOSTRE SUA PORÇÃO INTEIRA
"""
import math
num = float(input('Digite um número real: '))
print ('O valor digitado fio {} e a sua porção inteira é {}'.format(num, math.trunc(num)))