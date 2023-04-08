# Exercício - input e if

primeiro_valor = input('Primeiro valor: ')
segundo_valor = input('Segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} é maior que o {primeiro_valor=}')
