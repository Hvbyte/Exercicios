frase:str = '      Curso em Video Python      '
print(frase[1:15])  # LER DENTRO DOS ESPAÇOS DELIMITAOS#
print(frase[1:15:1])  # LER DE UM A 14 PULANDO UMA CARACTERE
print(frase.count('o'))  # QUANTAS LETRAS 'o'
print(frase.upper())  # LEVAR À MAIÚSCULAS
print(frase.lower())  # MINUSCULAS
print(len(frase))  # QUANTIDADE
print(len(frase.strip()))  # QUANTIDADE S ESPAÇOS R AND L
print(frase.replace('Video', 'Casa'))  # SUBSTITUIR
print('Curso' in frase)  # VERIFICAR SE CONTEM
print(frase.find('Curso'))  # POSIÇAO

dividido = frase.split()  # LISTA
print(dividido)
print(dividido[1][1])  # MOSTAR A SEGUNDA LETRA DA SEGUNDA PALAVRA
