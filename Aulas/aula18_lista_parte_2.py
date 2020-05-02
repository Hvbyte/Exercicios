'''#Adicionando itens em uma lista
dados = list()
dados.append('pedro')
dados.append(25)
print(dados[0])
print(dados[1])
#Criando uma cópia de dados dentro da lista pessoas
pessoas = list()
pessoas.append(dados[:])
print(pessoas)
#segue
pessoas = [['pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) #pedro
print(pessoas[1][1]) #19
print(pessoas[2][0]) #João
print(pessoas[1]) #['Maria', 19]
#teste
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 23
galera.append(teste[:])
print(galera)

#Usando laço for
galera = [['João,', 34],['Maria', 26],['Vicente', 89], ['Gabi', 34]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

#Coletando dados
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 2):
    dado.append((str(input('Nome: '))))
    dado.append((int(input('Idade: '))))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')

