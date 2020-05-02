palavras = ('aprender','programar','desenvolver','linguagem',
            'python','praticar','futuro','trabalhar','mercado',
            'curso','gratis')
for p in palavras:
    print(f'\nNas palavras {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')