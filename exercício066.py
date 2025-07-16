# -*- coding: utf-8 -*-
"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantas números foram digitados e qual foi a soma entre eles
"""

print()

n = int(input('Digite um número inteiro: '))
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break



