print(15*'-=')
print('GERADOR DE PG')
print(15*'-=')
P1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
ncontagem = 1
total = 0
n = 10
while n != 0:
    total += n
    while ncontagem <= total:
        print('{} ->'.format(P1), end='')
        P1 += r
        ncontagem += 1
    print('PAUSA')
    n = int(input(('Quantos termos você quer a mais?')))
print('FIM')

