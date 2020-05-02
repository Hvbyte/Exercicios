Salário = float(input('Qual é o salário do funcionário R$'))
Sb = Salário * 1.1
Sa = Salário * 1.15
if Salário > 1250:
    print('Quem ganhava R${:0.2f} passa a ganhar R${:0.2f} agora.'.format(Salário, Sa))
else:
    print('Quem ganhava R${:0.2f} passa a ganhar R${:0.2f} agora.'.format(Salário, Sb))
