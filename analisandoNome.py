#Programa lê o nome e mostra:
#Em letras MAIUSCULAS
#Em letras minusculas
#quantas letras ao todo (sem espaços)
#quantas letras tem primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando nome......')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))