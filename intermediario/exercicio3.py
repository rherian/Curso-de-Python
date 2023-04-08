# Perguntas e Respostas usando dicionário

resposta = ''
acertos = 0
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': [1, 3, 4, 5],
        'Resposta':4,
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': [25, 55, 10, 51],
        'Resposta':25,
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': [4, 5, 2, 1],
        'Resposta':5,
    },
]

for pergunta in perguntas:
    print(f'Pergunta: {pergunta["Pergunta"]}')
    for opcao in pergunta['Opções']:
        print(opcao)

    resposta = int(input('Digite o índice da resposta: '))
    if resposta == pergunta['Resposta']:
        print('\nACERTOU! 👍\n\n')
        acertos += 1
    else:
        print('\nERROU ❌\n\n')

print(f'\nVocê acertou {acertos} de {len(perguntas)} perguntas!\n')
