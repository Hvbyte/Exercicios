Casa = float(input('Qual o valor da casa: R$'))
Salário = float(input('Qual o seu salário: R$'))
Anos = int(input('Em quantos anos deseja pagar: '))
k = Salário * 0.30
Mensalidade = Casa // (Anos * 12)
print('Para pagar uma casa no valor de R${:.2f} em {:.0f} anos o pagamento mensal será de R${:.0f}.'.format(Casa, Anos, Mensalidade))
if k >= Mensalidade:
    print('Empréstimo pode ser concedido!')
else:
    k <= Mensalidade
    print('Empréstmio negado!')





print(k)





