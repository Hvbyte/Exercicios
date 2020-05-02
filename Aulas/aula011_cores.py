# STYLE
print('\033[1mOlá, Mundo!\033[m')
print('\033[4mOlá, Mundo!\033[m')
print('\033[7mOlá, Mundo!\033[m')
# CORES
print('\033[;30mOlá, Mundo!\033[m')
print('\033[;31mOlá, Mundo!\033[m')
print('\033[;32mOlá, Mundo!\033[m')
print('\033[;34mOlá, Mundo!\033[m')
print('\033[;35mOlá, Mundo!\033[m')
print('\033[;36mOlá, Mundo!\033[m')
print('\033[;37mOlá, Mundo!\033[m')
# FUNDOS
print('\033[;;40mOlá, Mundo!\033[m')
print('\033[;;41mOlá, Mundo!\033[m')
print('\033[;;42mOlá, Mundo!\033[m')
print('\033[;;43mOlá, Mundo!\033[m')
print('\033[;;44mOlá, Mundo!\033[m')
print('\033[;;45mOlá, Mundo!\033[m')
print('\033[;;46mOlá, Mundo!\033[m')
print('\033[;;47mOlá, Mundo!\033[m')

Nome = 'Higor'
print('Olá,{}{}{}! Tudo bem com você?'.format('\033[1;31;7m', Nome, '\033[m'))

# OU

Nome = 'Higor'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[32m',
         'pretoebranco':'\033[7;30m'}

print('Olá,{}{}{}! Tudo bem com você?'.format(cores['azul'], Nome, cores['limpa']))




