# -*- coding: utf-8 -*-
"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

print()

matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = 0 

for l in range(0, 3):
    
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o valor [{l+1, c+1}]: "))

t_soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print()

if matriz[1][0] > matriz[1][1] > matriz[1][2]:
    maior = matriz[1][0]
    
elif matriz[1][1] > matriz[1][0] > matriz[1][2]:
    maior = matriz[1][1]
    
elif matriz[1][2] > matriz[1][1] > matriz[1][0]:
    maior = matriz[1][2]

elif matriz[1][0] > matriz[1][2] > matriz[1][1]:
    maior = matriz[1][0]

elif matriz[1][1] > matriz[1][2] > matriz[1][0]:
    maior = matriz[1][1]
    
elif matriz[1][2] > matriz[1][0] > matriz[1][1]:
    maior = matriz[1][2]
 
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^ 5}]', end='')
    print()

maior
print()
print(f'A soma de todos os termos dessa matriz é {soma}.')
print()
print(f'A soma dos valores da terceira coluna é {t_soma}.')
print()
print(f'O maior número da segunda linha é {maior}.')


    






