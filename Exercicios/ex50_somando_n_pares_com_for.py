'''DESENVOLVA UM PROGRAMA QUE
LEIA SEIS NÚMEROS INTEIROS E
MOSTRE A SOMA APENAS DAQUELES
QUE FOREM PARES. SE O VALOR
DIGITADO FOR ÍMPAR ,DESCONSIDERE-O.'''

soma = 0
cont = 0
for n in range(1, 7):
        num = int(input('Digite o {}° valor:'.format(n)))
        if num % 2 == 0:
            soma += num
            cont = cont + 1

print('Você informou {} números PARES e a soma foi {}.'.format(cont, soma))

