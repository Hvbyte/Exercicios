mil = cont = menorv = valort = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço: R$'))
    resp = str(input('Quer continuar?[S/N]')).upper().strip()
    valort += preço
    cont += 1
    if preço >= 1000:
        mil += 1
    if mil > 1:
        s = 's'
    if cont == 1 or preço <= menorv:
        menorv = preço
        barato = produto
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${valort}.')
print(f'Temos {mil} produto{s} custando mais de R$1000. ')
print(f'O produto mais barato foi {barato} e custou R${menorv}.')