print('-='*20)
print('Analizador de Triãngulos')
print('-='*20)
r1 = float(input('Informe o primeiro segmentos de reta: '))
r2 = float(input('Informe o segundo segmentos de reta: '))
r3 = float(input('Informe o terceiro segmentos de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos aciama NÃO PODEM FORMAR triângulo!')