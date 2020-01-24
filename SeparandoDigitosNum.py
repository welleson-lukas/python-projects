#separando digitos de numeros ate 9999
#unidades, dezenas, centenas, milhares
num = int(input('Digite o numero: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Milhares {}'.format(m))
print('Centenas {}'.format(c))
print('Dezenas {}'.format(d))
print('Unidades {}'.format(u))
