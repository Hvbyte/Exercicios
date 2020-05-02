from random import randint
from time import sleep
nc = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 a 5. Tente advinhar...')
print('-=-'*20)
np = int(input('Em qual número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if nc == np:
    print('Parabéns você venceu!')
else:
    print('Você perdeu!')
    print('O número que escolhi foi o {} e não o {} :('.format(nc, np))


