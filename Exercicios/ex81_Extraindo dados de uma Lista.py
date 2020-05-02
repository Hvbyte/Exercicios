lista = []
plural = ' '
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ''
    resp = str(input('Que continuar? [S/N]: ')).upper().strip()[0]
    while resp not in 'NS':
        resp = str(input('Que continuar? [S/N]: ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')