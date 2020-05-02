'''DESENVOLVA UM PROGRAMA QUE LEIA
O PRIMEIRO TERMO E A RAZÃO DE UMA PA.
NO FINAL MOSTRE OS 10 PRIMEIRO
TERMOS DESSA PROGRESSÃO'''

primeiro = int(input('Primeiro termo:' ))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão

for c in range(primeiro, decimo + razão, razão):
    print('{}'.format(c), end='-> ')
print('ACABOU')
