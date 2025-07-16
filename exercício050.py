# -*- coding: utf-8 -*-
"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor 
digitado for ímpar, desconsidere-o.
"""

print()

soma = 0
for i in range(6):
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        soma = soma + n

print("A soma dos números pares é {}.". format(soma))