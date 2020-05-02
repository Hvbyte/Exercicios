n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
M = (n1 + n2)/ 2
print('Sua media foi {}.'.format(M))
if 5 <= M <= 6.9:
    print('RECUPERAÇÃO!')

elif M < 5:
    print('REPROVADO!')

elif M >= 7:
    print('APROVADO!')