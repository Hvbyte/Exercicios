dias = int(input('Quantidade de dias com o veículo:'))
KM = float(input('Quantos Km rodados:'))
preço = dias * 60 + KM * 0.15
print('O valor do alugel é: R${}'.format(preço))
