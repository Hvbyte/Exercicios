'''CRIE UM PROGRAMA QUE LEIA
UMA FRASE QUALQUER E DIGA
SE ELE É UM POLÍNDROMO.
DESCONSIDERE OS ESPAÇOS


frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
   inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não NÃO É PALÍNDROMO.')






OUTRA FORMA DE SE REALIZAR SEM UTILIZAR O FOR

frase = str(input('Digite uma frase:')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não NÃO É PALÍNDROMO.'''






frase = input('frase: ')
palavras = frase.split()
junto = frase.join(palavras)
inverso = ''

for letras in range(len(frase)-1, -1, -1):
    print(junto[letras], end='')






    '''if inverso == frase:
        print('é polindromo', end = ' ')
    else:
        print('n é polindromo')
print('a frase inversa é {}.'.format(inverso), end= ' ')'''


