num = (int(input('Digite o primeiro número: ')),
        int(input('Digite o segundo número: ')),
        int(input('Digite o terceiro número: ')),
        int(input('Digite o quarto e último número: ')))

print(f'Você digitou os seguintes valores:{num}.')
print(f'você digitou o número 9 {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 foi digitado na {num.index(3)+1}ª posição.')
else:
    print(f'O número 3 não foi digitado nenhuma vez.')
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end = '')
