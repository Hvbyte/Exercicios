Preço = float(input('Qual o preço do produto: R$'))
Desconto = float(input('Qual o desconto pretendido: %'))
Valor = Preço * (- Desconto/100 + 1)
print("O produto escolhido com o desconto de {}% terá como valor final R${}".format(Desconto, Valor))