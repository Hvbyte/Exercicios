a = int(input('Primeiro valor: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
print(' O menor valor digitado foi {}'.format(menor))
print(' O maior valor digitado foi {}'.format(maior))
