total18 =totH = totm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    resp = ' '
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade >= 20:
        totm20 += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas maiores de 18 anos: {total18}')
print(f'Ao total temos {totH} homens cadastrados')
print(f'E temos {totm20} mulheres maiores de 20 anos')
