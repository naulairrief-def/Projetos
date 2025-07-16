# -*- coding: utf-8 -*-
"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, 
mostre uma listagem de preços, organizando os dados em forma tabular.
"""

print()
print('{:^80}'.format('LISTAGEM DE PRODUTOS'))
print("=" * 80)

dados = ('Lápis', 1.50,
         'Caneta', 2.00,
         'Borracha', 3.00,
         'Estojo', 5.00,
         'Caderno', 15.00,
         'Mochila', 50.00,
         'Lapiseira', 7.00,
         'Canetinha', 5.00,
         'Livro', 50.00)

print()

for produto in range(0, len(dados)):
    if produto % 2 == 0:
        print(f'{dados[produto]:.<70}', end= '')
    else:
        print('R$',f'{dados[produto]:>7.2f}')
print()
print("=" * 80)