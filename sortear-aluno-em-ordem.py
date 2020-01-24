"""
LEIA NOME DE ALUNOS E SORTEIE UMA ORDEM ALEATORIA
"""
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem será: ')
print(lista)

###############################
from random import shuffle
n1 = str('Lukas')
n2 = str('Gabriel')
n3 = str('Raimundo')
n4 = str('Jhonatan')
n5 = str('Raisse')
n6 = str('Izael')
n7 = str('Fabricio')
n8 = str('Naelton')
lista = [n1, n2, n3, n4, n5, n6, n7, n8]
shuffle(lista)
print('A ordem será: ')
print(lista)
################################