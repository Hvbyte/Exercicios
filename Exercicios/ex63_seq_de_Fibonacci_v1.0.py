n = int(input('Digite o número de termos que você quer mostrar: '))
Nant = 1
Fiboncci = 0
while n != 0:
    print('{} ->'.format(Fiboncci), end='')
    Fiboncci = Fiboncci + Nant
    Nant = Fiboncci - Nant
    n -= 1
print('FIM')