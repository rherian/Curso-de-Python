# Jogo de adivinhação de palavras

''' 
- Pedir ao usuário uma letra
- Conferir se há a letra na palavra secreta
- Retornar a posição da letra na palavra secreta e substituir na string para o usuario
'''

palavra = 'Vasco'.upper()
letras_certas = ''
tentativas = 0


while True:
    tentativas += 1

    letra = input('Digite uma letra: ').upper()

    if len(letra) > 1 or len(letra) == 0:
        print('\nDigite uma letra.')
        continue

    if letra in palavra:
        letras_certas += letra

    palavra_formada = ''
    for letra_digitada in palavra:
        if letra_digitada in letras_certas:
            palavra_formada += letra_digitada
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra:
        print('\n\nVOCÊ ACERTOU!')
        print(f'Número de tentavais: {tentativas}')
        print(f'Palavra: {palavra}')
        break
