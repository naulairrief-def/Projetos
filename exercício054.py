# -*- coding: utf-8 -*-
"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.
"""

print()
k = 0
c = 0
for i in range(1, 8):
    print()
    nome = str(input("Digite o nome da pessoa: "))
    nasc = int(input("Digite o ano de nascimento: "))
    idade = 2024 - nasc
    
    if idade < 18:
        #print("{} ainda não é de maior.". format(nome))
        k += 1
        
    else:
        #print("{} já é de maior.". format(nome))
        c += 1
print()
print("Ao todo, temos {} de menores.". format(k))
print()
print("Ao todo, temos {} de maiores.". format(c))