preco = float(input('Qual o valor do produto? R$ '))
desconto = float(input('Qual a porcentagem de desconto? '))

novo = preco - (preco * desconto /100)
print('O prduto que custava R$ {:.2f}, na promoção de {}% de desconto, vai custar R$ {:.2f}'.format(preco, desconto, novo))