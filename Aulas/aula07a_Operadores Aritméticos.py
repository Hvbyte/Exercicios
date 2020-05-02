

##########Operadores Aritiméticos#############




nome = input('Qual o seu nome?')
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {},\n a divisão é {:.3f}\n'.format(s, m, d), end=' ')
print('Divisão inteira {}\n e potência {:.3f}\n'.format(di, e))









