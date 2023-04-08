# exercicio sobre funcoes e desempacotamentod de parametros


def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


def par_impar(numero):
    print('Par') if numero % 2 == 0 else print('Impar')


resultado = multiplicacao(9, 21)
print(resultado)
par_impar(resultado)
