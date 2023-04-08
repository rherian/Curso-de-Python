# Algoritmo para contagem de letras de uma string


frase = 'VASCO DA GAMA E NADA MAIS'

i = 0

maior_repeticao = 0
letra_mais_repetida = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    repeticao_atual = frase.count(letra_atual)

    if maior_repeticao < repeticao_atual:
        maior_repeticao = repeticao_atual
        letra_mais_repetida = letra_atual

    i += 1
print(frase)
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_repetida}" que apareceu '
    f'{maior_repeticao}x\n\n'
)
