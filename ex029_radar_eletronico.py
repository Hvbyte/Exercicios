from time import sleep
velocidade = float(input('Qual a velocidade atual do carro? '))
print('Um instante...')
sleep(2)
multa = (velocidade - 80) * 7
if velocidade>80:
    print('MULTADO! Você está acima da velocidade permitida que 80Km/h ')
    print('Você deve pagar uma multa no valor R${:.2f}'.format(multa))
print('Tenha um bom dia! Diriga com segurança!')