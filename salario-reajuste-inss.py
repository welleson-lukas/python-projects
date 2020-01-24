print('CALCULE SEU SÁLARIO E OS DESCONTOS')

salario = float(input('Digite seu sálario? R$ '))
fgts = (salario * 8 / 100)
inss = (salario * 8 / 100)
salariopordia = (salario / 30)
salarioliquido = (salario - inss)

print('Sálario bruto: R$ {}'.format(salario))
print('Desconto do INSS: R$ {}'.format(inss))
print('O FGTS desse mês é: R$ {}'.format(fgts))
print('O salario liquido é: R$ {}'.format(salarioliquido))
