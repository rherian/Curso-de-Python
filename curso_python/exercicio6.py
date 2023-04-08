# Exercicio - repeticao com while

nome = input('Nome: ')
contador = 0
tamanho_nome = len(nome)

while contador < tamanho_nome:
    if contador == 0:
        print('*', end='')

    print(nome[contador]+'*', end='')
    contador += 1
