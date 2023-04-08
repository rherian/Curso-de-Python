# Exercicio - Calculadora com while
print('CALCULADORA')
while True:

    try:
        numero1 = int(input('Digite o primeiro número: '))
        operacao = input('Digite a operacao desejada (+ - * /): ')
        numero2 = int(input('Digite o segundo número: '))
        resultado = 0

        if operacao == '+':
            resultado = numero1 + numero2
        elif operacao == '-':
            resultado = numero1 - numero2
        elif operacao == '*':
            resultado = numero1 * numero2
        elif operacao == '/':
            resultado = numero1 / numero2
        else:
            print('Operação inválida!')

        print(numero1, operacao, numero2, '=', resultado)

    except:
        print('Digite um número inteiro!')

    sair = input('\nDeseja sair? ').lower().startswith('s')
    if sair is True:
        break
