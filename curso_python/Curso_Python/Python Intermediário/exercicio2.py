'''Criar um algoritmo que duplica, triplica e quadruplica um numero usando recursividade e closure de funções'''


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(5))
print(duplicar(2))
