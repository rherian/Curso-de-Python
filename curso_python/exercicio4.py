# Exercício - fatiamento de strings e operadores logicos

nome = input('Nome: ')
idade = input('Idade: ')
nome_invertido = nome[::-1]
tamanho_nome = len(nome)


if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if ' ' in nome:
        print('Seu nome contem espaços')
        print(f'Seu nome tem {tamanho_nome-1} letras')
    else:
        print('Seu nome não contém espaços')
        print(f'Seu nome tem {tamanho_nome} letras')

    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')
