real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 3.76
euro = real / 4.21
print('Com R$ {:.2f} você pode comprar US${:.2f} dolares e €{:.2f} euros'.format(real, dolar, euro))
