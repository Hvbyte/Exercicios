n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('>>>>>Digite sua opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1 * n2
        print('O resultado entre {} x {} é {}.'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os valores novamente:')
        n1 = input('Digite o primeiro valor:')
        n2 = input('Digite o segundo valor:')
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente')
    print('-=-'*10)
print('Fim de programa! Volte sempre!')
