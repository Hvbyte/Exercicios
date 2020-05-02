'''FAÇA UM PROGRAMA QUE CALCULE
A SOMA ENTRE TODOS NÚMEROS ÍMPARES
QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE
ENCONTREM NO INTERVALO DE 1 ATÉ 500'''

soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        cont = cont + 1
print('A soma entre os {} valores solicitados é {}.'.format(cont, soma))