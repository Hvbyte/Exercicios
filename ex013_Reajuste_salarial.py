Sal = float(input('Qual é o salário do funcionário? R$'))
Aumento = float(input('Qual a porcentagem de aumento: %'))
Salf = Sal*(Aumento/100+1)
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber {:.2f}'.format(Sal, Aumento, Salf))