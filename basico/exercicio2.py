# '...' são elipses e não geram ao erro quando estão atribuidas a uma variavel

# Exercicio - f strings

nome = 'Luiz Otavio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

print(f'{nome} tem {altura:.2f} de altura,\npesa {peso} quilos e seu imc é {imc:.2f}')
