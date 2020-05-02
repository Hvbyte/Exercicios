S1 = float(input('Primeiro seguimento: '))
S2 = float(input('Segundo seguimento: '))
S3 = float(input('Terceiro seguimento: '))
if S1 + S2 > S3 and S1 + S3 > S2 and S3 + S2 > S1:
    print(' Os seguimentos {:.0f}, {:.0f} e {:.0f} PODEM  formar um triângulo'.format(S1, S2, S3), end=' ')
    if S1 == S2 == S3:
        print('EQUILÁTERO !')
    elif S1 == S2 != S3 or S2 == S3 != S1 or S1 == S3 != S2:
        print('ISÓCELES !')
    else:
        S1 != S2 != S3
        print('ESCALENO !')
else:
    print(' Os seguimentos {:.0f}, {:.0f} e {:.0f} NÃO PODEM formar um triângulo'.format(S1, S2, S3))
