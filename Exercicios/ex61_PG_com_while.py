Primeiro = int(input('Digite o primeiro termo da sua PG: '))
Razão = int(input('Razão :'))
n = int(input('Digite a quantidade termos: '))
termo = Primeiro
cont = 1
while cont <= n:
    print('{} -> '.format(termo), end= '')
    termo += Razão
    cont += 1
print('FIM')