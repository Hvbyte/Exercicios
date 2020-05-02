print('='*30)
print('{:^30}'.format('BANCO HVO'))
print('='*30)
valor = int(input('Qual valor você quer sacar?'))
céd = 50
total = valor
totced = 0
while True:
    if total >= céd:
        total -= céd
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédeulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totced = 0
        if total == 0:
            break



valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)
nota = 0
while nota in {50, 20, 10, 1}:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
if quantidade > 0:
    print(f'{quantidade} notas de R$ {nota}')