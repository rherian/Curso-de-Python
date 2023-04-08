# Gerador de CPF

import random

nove_digitos = ''
cpf_gerado = ''

for _ in range(9):
    nove_digitos += str(random.randint(0, 9))

resultado1 = 0
resultado2 = 0
contador_regressivo1 = 10
contador_regressivo2 = 11


# PRIMEIRO DIGITO
for numero in nove_digitos:
    resultado1 += int(numero) * contador_regressivo1
    contador_regressivo1 -= 1


resultado1 = (resultado1 * 10) % 11

digito1 = 0 if resultado1 > 9 else resultado1
cpf_gerado += nove_digitos + str(digito1)


for numero in cpf_gerado:
    resultado2 += int(numero) * contador_regressivo2
    contador_regressivo2 -= 1


resultado2 = (resultado2 * 10) % 11

digito2 = resultado2 if resultado2 < 9 else 0

cpf_gerado = nove_digitos + str(digito1) + str(digito2)

print(cpf_gerado)
