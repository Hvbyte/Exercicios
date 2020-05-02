from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a pessoa {}ª pessoa nasceu?: '.format(pess)))
    idade = atual - nasc
    if 18 <= idade:
        totmaior += 1
    else:
        idade <= 18
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade!'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade!'.format(totmenor))