from datetime import date
atual = date.today().year
sexo = int(input('''Qual o seu sexo?
[ 1 ] FEMININO
[ 2 ] MASCULINO
Digite o número correspondente: '''))
if sexo == 1:
    sn = str(input('Você não é obrigada a se alistar, deseja continuar?')) .strip().lower()
    if sn == 'sim':
        ano = int(input('Em qual ano você nasceu? '))
        idade = atual - ano
        if idade == 18:
            print('Você deve se alistar IMEDIATAMENTE!')
        elif idade > 18:
            saldo = idade - 18
            print('Você deveria ter se alistado há {} anos.'.format(saldo))
            ano = atual - saldo
            print('seu alistamento foi em {}.'.format(ano))
        elif idade < 18:
            saldo = 18 - idade
            print('Você deve se alistar daqui a {} anos.'.format(saldo))
            ano = atual + saldo
            print('Seu alistamento será em {}'.format(ano))
else:
    sexo == 2
    ano = int(input('Em qual ano você nasceu? '))
    idade = atual - ano
    if idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!')
    elif idade > 18:
        saldo = idade - 18
        print('Você deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('seu alistamento foi em {}.'.format(ano))
    elif idade < 18:
        saldo = 18 - idade
        print('Você deve se alistar daqui a {} anos.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
