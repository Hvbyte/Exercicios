lista = ('Lápis' , 1.43,
         'Borracha', 0.75,
         'Caderno', 16.89,
         'Estojo', 7,
         'transferidor',5.8,
         'Compasso', 4.8,
         'Mochila',80.68,
         'Canetas',8.56,
         'Livros',39.9,)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}R$',end='')
    else:
        print(f'{lista[pos]:>7}')
print('-'*40)