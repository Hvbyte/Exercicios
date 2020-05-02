maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Digite o número da {}ª pessoa: '.format(pess)))
    if pess == 1:
         maior = peso
         menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso lido foi o de {}Kg'.format(maior))
print('Menor peso lido foi o de {}Kg.'.format(menor))




