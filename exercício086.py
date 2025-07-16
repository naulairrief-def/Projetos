# -*- coding: utf-8 -*-
"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre
a matriz tabela, com a formatação correta.
"""

'Solução 1'
print()
'''print('VAMOS AGORA DIGITAR UMA MATRIZ 3X3')
p_linha = []
s_linha = []
t_linha = []
print()

for p in range(1, 4):
    n = int(input(f"Digite o {p}° valor da primeira linha: "))
    p_linha.append(n)

for s in range(4, 7):
    m = int(input(f"Digite o {s}° valor da segunda linha: "))
    s_linha.append(m)
    
for t in range(7, 10):
    o = int(input(f"Digite o {t}° valor da terceira linha: "))
    t_linha.append(o)

matriz = [p_linha, 
          s_linha, 
          t_linha]

print()

print(matriz[0])
print(matriz[1])
print(matriz[2])'''



'Solução 2'

ma = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(0, 3):
    for c in range(0, 3):
        ma[i][c] = int(input(f"Digite um valor para a posição [{i}, {c}]: "))
        

print()
print('=' * 50)

for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{ma[i][c]:^4}]', end= '')
    print()








