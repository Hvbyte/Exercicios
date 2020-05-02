sexo = input(str('Insira seu sexo [M / F]:')) .strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input(str('Dados inválidos, por favor, informe seu sexo: '))
print('Sexo {} informado com sucesso.'.format(sexo))