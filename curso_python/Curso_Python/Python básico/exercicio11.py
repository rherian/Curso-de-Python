# VALIDAÇÃO DE CPF - BÁSICO

'''
    CALCULO PARA VALIDACAO DO PRIMEIRO DIGITO DO CPF
- Somar os nove primeiros digitos do CPF
- Multiplicar cada digito em uma contagem regressiva começando em 10 e somar 
- Multiplicar o resultado da soma por 10
- Pegar o resto da divisão entre o valor anterior por 11
- Caso o resto seja > 9, o numero será 0, se não, o número será o resto da divisão


    CALCULO PARA VALIDACAO DO SEGUNDO DIGITO DO CPF
- Somar os 9 primeiros digitos do CPF + o primeiro digito obtido anteriormente
- Multiplicar cada digito em uma contagem regressiva começando em 11 e somar
- Após isso, repetir o restante feito na operação do primeiro digito

'''

cpf = input('CPF: ')
resultado1 = 0
resultado2 = 0
contador_regressivo1 = 10
contador_regressivo2 = 11
cpf_numeros = ''

for numero in cpf:
    if numero == '.' or numero == '-':
        continue
    else:
        cpf_numeros += numero


# PRIMEIRO DIGITO
for numero in cpf_numeros:
    resultado1 += int(numero) * contador_regressivo1
    contador_regressivo1 -= 1
    if contador_regressivo1 == 1:
        break

resultado1 = (resultado1 * 10) % 11

digito1 = 0 if resultado1 > 9 else resultado1
cpf_numeros += cpf_numeros + str(digito1)

for numero in cpf_numeros:
    resultado2 += int(numero) * contador_regressivo2
    contador_regressivo2 -= 1
    if contador_regressivo2 == 1:
        break

resultado2 = (resultado2 * 10) % 11

digito2 = resultado2 if resultado2 < 9 else 0

validacao = True if str(
    digito1) == cpf[-2] and str(digito2) == cpf[-1] else False

if validacao:
    print(f'\nCPF {cpf} válido!\n')
else:
    print('\nCPF inválido!\n')
