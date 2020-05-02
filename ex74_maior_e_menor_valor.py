from random import randint
n = (randint(1,10), randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores sorteados foram:{n[0:]}',)
print(f'O maior valor sorteado da tupla foi: {max(n)}')
print(f'O menor valor sorteado foi: {min(n)}')