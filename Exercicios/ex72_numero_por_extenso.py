ext = ('zero', 'um', 'dois','tres','quatro','cinco','seis',
       'sete','oito','nove','dez','onze','doze','treze',
       'catorze','quinze','dezesseis','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número de 0 a 20:'))
    if 0 <= num <= 20:
        break
    print('Tente novamente...',end='')
print(f'O número que você digitou foi {ext[num]}.')