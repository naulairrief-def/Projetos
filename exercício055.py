# -*- coding: utf-8 -*-
"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
print('-' * 100)

print('Vamos ler os pesos de 5 pessoas e extrair o maior e o menor peso respectivamente.')
print()
menor = maior = 0

for i in range(6):
    peso = float(input("Digite o peso desta pessoa: "))
    if i == 1:
        menor = maior
    else:
        if peso > maior:
            maior = peso
            
        if peso < menor:
            menor = peso

print()
            
print(f'O maior peso lido foi {maior}Kg.')
print()
print(f'O menor peso lido foi {menor}Kg.')
