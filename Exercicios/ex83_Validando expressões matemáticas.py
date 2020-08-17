exp = input('insira uma expressão para análise: ')
if exp.count('(') == exp.count(')'):
    print('Sua expressão é valida!')
else:
    print('Sua expressão NÃO é válida!')

expr = str(input(f'Digite sua expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append(símb)
    elif símb == ')':
        if len(pilha) == 0:
            pilha.append(símb)
        else:
            pilha.pop()
if 0 == len(pilha):
    print(f'Sua expressão é válida! ')
else:
    print(f'Sua expressão não é válida!') 
  