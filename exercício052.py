# -*- coding: utf-8 -*-
"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
print()
n = int(input("Digite um número: "))

for i in range(1, n + 1):
    print(end = '')
if n % i == 0 and n != 1:
    print("O número {} é primo.". format(n))
    
else:
    print("O número {} não é primo.". format(n))
    