'''FAÇA UM PROGRAMA QUE LEIA
UM NÚMERO INTEIROE DIGA
SE ELE É PRIMO OU NÃO UM NÚMERO PRIMO'''

tot = 0
num = int(input('Digite um número: '))

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[0;32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divísivel {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso, ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')