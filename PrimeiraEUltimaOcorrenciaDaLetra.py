#PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#QUANTAS VEZES APARECE A LETRA 'A"
#EM QUAL POSIÇÃO ELE APARECE PELA PRIMEIRA E ULTIMA VEZ
frase = str(input('Digite uma frase: ')).upper().strip()#upper()fara a conversão das strings para maiusculas #strip() não permite que os espaço sejam contados na entrada de texo
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))