# LISTA

lanche = ['hamburguer', 'suco','pizza', 'pudim',]
print(lanche)
lanche[3] = 'picolé'
print(lanche)

#ADICIONANDO

lanche.append('biscoito')#Adicionando na item no fim da lista
lanche.insert(0,'hot-dog')#Adicionando em um índice específico

#ELIMINANDO

del lanche[3]#Eliminar em um índice específico


lanche.pop(3)#Eliminar pelo indice(sem índice remove o último)

lanche.remove('suco')#Eliminar pelo o produto do índice
if 'suco' in lanche:
    lanche.remove('suco')

#ORGANIZANDO


valores = [8,6,7,5,4,3,1,2,0]
valores.sort()
valores.sort(reverse=True)
print(valores)

#CONTANDO

print(len(valores))

#LISTA COM INPUT

valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um número: ')))
for c, v in enumerate(valores):
    print(f'Você digitou na {c+1}ª posição os valores: {v}')

#DESVINCULANDO DUAS LISTAS
a = [1,3,4,3]
b = a[:]
b[0] = 90
print(f'Lista A: {a}')
print(f'Lista B: {b}')