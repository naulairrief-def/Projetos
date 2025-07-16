# -*- coding: utf-8 -*-
"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada em forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

print()

cont = 0
valores = []
for i in range(0,10):
    num = int(input("Digite um número: "))
    cont += 1
    valores.append(num)

valores.sort()
valores.sort(reverse=True)

print()
print(f'{cont} números foram digitados.')
print()
print(valores)
print()
if 5 in valores:
    print('O número 5 aparece na lista.')
    
else:
    print('O número 5 não aparece na lista.')
    
