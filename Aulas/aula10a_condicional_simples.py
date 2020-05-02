#CONDIÇÃO SIMOLES#

nome = str(input('Qual o seu nome?'))
if nome == 'Higor':
    print('Que nome lindo você tem!')
print('Bom dia, {}'.format(nome))

'''--------------------------------------'''



n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
m = (n1 + n2)/2
print('Sua média é {:.1f}'.format(m))
if m>=6:
    print('Parabens! você passou.')
else:
    print('Sua média foi ruim. Estude mais!')


