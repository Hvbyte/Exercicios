D = float(input('Qual a distância de sua viagem:'))
if 200 > D:
    print('Sua viagem custará R${:.2f}.'.format(D*0.50))
else:
    print('Sua viagem custará R${:.2f}.'.format(D*0.45))
P = str(input('Você quer confirmar a viagem?')).upper().strip()
print(P)
if P == 'SIM':
    print('Seu carro está a caminho, tenha uma boa viagem!')
else:
    print('Sua chamada foi cancelada!')


