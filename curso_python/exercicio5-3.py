# Exercicio - função len e operadores logicos
nome = input('Digite seu nome: ')

tamanho = len(nome)

if tamanho > 1:
    if tamanho <= 4:
        print('Seu nome é curto')
    elif tamanho >= 5 and tamanho <= 6:
        print('Seu nome é normal')
    elif tamanho > 6:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
