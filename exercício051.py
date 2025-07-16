# -*- coding: utf-8 -*-
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos 
dessa progressão.
"""

print()
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
print()
print("Os termos da PA descrita são:")

for n in range(primeiro, primeiro + 10*razao, razao):
    print(n, end = ' ')