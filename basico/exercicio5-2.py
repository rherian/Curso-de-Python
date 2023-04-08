# Exercicio - if e operadores logicos

horario = input("Digite o horário: ")

hora = int(horario[0:2])

if hora <= 11:
    print('Bom dia!')
elif hora >= 11 and hora <= 17:
    print('Boa tarde!')
elif hora >= 18 and hora <= 23:
    print('Boa noite!')
else:
    print('Hora desconhecida')
