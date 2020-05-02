#Exercício Python 082: Crie um programa que vai ler
# vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.



lista01 = []
lista02 = []
lista03 = []
while True:
    num = int(input('Digite um número: '))
    lista01.append(num)
    if num % 2 == 0:
        lista02.append(num)
    else:
        lista03.append(num)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    while resp not in 'SN':
        resp = str(input(f'Resposta inválida! Tente novamente. Quer continuar? [S/N] ')).upper().strip()
    if resp in 'N':
        break
if len(lista02) == 0:
    lista02.append('Nenhum valor')
else:
    lista03.append('Nenhum valor')
print('*'*30)
print(f'A lista completa é {lista01}')
print(f'A lista dos pares {lista02}')
print(f'A lista dos ímpares {lista03}')
print('*'*30)