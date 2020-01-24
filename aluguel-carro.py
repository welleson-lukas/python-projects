"""
CALCULAR O PREÇO A PAGAR A PARTIR QUANTIDADE DE KM PERCORRIDOS E QUANTIDADE DE DIAS
1 DIA = 60 REAIS
1 KM = 0,15 REAIS
"""
print('CALCULAR VALOR DE ALUGUEL POR DIAS E KM')
dias = int(input('Quantos dias alugados? '))
quilometro = int(input('Quantos Km rodados? '))

alugueldias = dias * 60
aluguelkm = quilometro * 0.15
total = alugueldias + aluguelkm

print('O total a pagar é de: R$ {:.2f}'.format(total))
