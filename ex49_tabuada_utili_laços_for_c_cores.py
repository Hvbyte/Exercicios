'''FAÇA O DESÁFIO 009,
MOSTRANDO A TABUADA DE UM NÚMERO
QUE O USUÁRIO ESCOLHER,
SÓ QUE AGORA UTILIZANDO UM LAÇO FOR '''


num = int(input('{}Digite um número para ver sua tabuada:{} '.format('\033[1;31;40m','\033[m')))
print('-='*20)
for c in range(1, 11):
    print('\033[0;32m{} x \033[0;36m{:2} = \033[0;37m{}'.format(num, c, num*c))
print('-='*20)