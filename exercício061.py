# -*- coding: utf-8 -*-
"""
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
"""

print()
a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))

cont = 1
termo = a1

print()

while cont < 11:
    print(termo, end= ' ')
    
    termo = a1 + cont * r
    cont += 1
    
    