num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
    print('Valor adicionado com sucesso...')
    resp = input('Quer continuar? [S/N]')
    if resp in 'Nn':
        break
print('=-'*30)
num.sort()
print(f'Você adicionou os valores{num}')