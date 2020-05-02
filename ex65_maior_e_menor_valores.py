resp = 'S'
soma = cont = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            num = menor
    resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
print('A média dos números digitados é de {}; o maior número foi {} e {} o menor.'.format(soma//cont, maior, menor))
