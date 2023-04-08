# Exercicio - casos básicos com try e except

numero = input("Digite um numero inteiro: ")

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é um numero par')
    else:
        print(f'{numero} é um numero impar')
except:
    print(f'{numero} não é um inteiro')
