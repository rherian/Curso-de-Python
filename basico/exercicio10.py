'''
- Fazer uma lista de compras com listas em python
- O usuário deve poder inserir, apagar e listar valores da sua lista
- O programa não pode "quebrar" com erros de índices inexistentes;
'''
import os

lista_compras = []

while True:
    item = input('Item para lista de compras (S para sair): ').upper()

    if item == 'S':
        break

    lista_compras.append(item)

    for indice, item in enumerate(lista_compras):
        print('\t', indice, item)
##########################################

os.system('cls')
print('#'*5, 'LISTA PARCIAL', '#'*5, '\n')
for indice, item in enumerate(lista_compras):
    print('\t', indice, item)


##########################################
while True:
    decisao = input(
        '\n[A]dicionar, [R]etirar ou [S]air ').upper()

    if decisao == 'R':
        for indice, item in enumerate(lista_compras):
            print('\t', indice, item)
        retirada = int(
            input('\nDigite o indice do item ao qual deseja retirar da lista: '))
        try:
            lista_compras.pop(retirada)
        except:
            print('Não foi possível apagar este indice')

    elif decisao == 'A':
        adicionar = input(
            '\nDigite o item que deseja adicionar a lista de compras: ').upper()
        lista_compras.append(adicionar)

    elif decisao == 'S':
        os.system('cls')
        print('\n\n\n\tLISTA FINAL DE COMPRAS\n')
        for indice, item in enumerate(lista_compras):
            print('\t', indice, item)
        break
