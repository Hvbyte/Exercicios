ano = int(input('Qual ano você quer analisar: '))
if ano % 4 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} nâo é BISSEXTO'.format(ano))
