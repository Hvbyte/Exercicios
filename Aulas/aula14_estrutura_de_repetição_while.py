'''#QUANDO EU SEI O INÍCIO E O FIM

for c in range(1, 10):
    print(c)
print('FIM')

#NÃO HÁ NECESSIDADE DE SABER O FIM
c = 1
while c < 10:
    print(c)
    c = c + 1


#EXEMPLO DE QUANDO NÃO SEI O FIM
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')'''

#EXEMPLO COM NÚMEROS INFINITOS
par = ímpar = 0
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            ímpar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par,ímpar))
