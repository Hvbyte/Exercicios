n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('Sua soma vale {}.'.format(s))

# f strings

idade = 33
print(f'a data {idade:.2f}.') # nº de casas
print(f'a data {idade:^20}.') # centralizar
