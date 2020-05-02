# TIPOS PRIMITIVOS #
#INT()    EX: 7 + 5 = 12
#FLOAT()       EX: 0.098 , -0.5
#BOOL()    TRUE OU FALSE
#STR()    PALAVRAS, NUMEROS (ENTRE ASPAS)
#bool
n = bool(input('Digite um valor:'))
print(n)
#float
n = float(input('Digite um valor:'))
print(n)
#int
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
#str
n = input('Digite um valor:')
print(n.isnumeric())