times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-MG', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('=-'*15)
print(f'Lista de times do Brasileiro: {times}')
print(f'-='*15)
print(f'Os 5 primeiros são {times[:5]}')
print(f'-='*15)
print(f'Os 4 últimos são {times[-4:]}')
print(f'-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'-='*15)
print(f'A Chapecoense posição está na {times.index("Chapecoense")+1}ª posição')
