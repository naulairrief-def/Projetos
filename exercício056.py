# -*- coding: utf-8 -*-
"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    --> A média de idade do grupo.
    --> Qual é o nome do homem mais velho do grupo.
    --> Quantas mulheres tem menos de 20 anos.
"""

print()

cont = 0
soma = 0
velho = ''
velho_idade = 0

for i in range(4):
    print()
    
    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade da pessoa: "))
    sexo = str(input("Digite o sexo da pessoa[H/M]: ")).upper()
    
    soma = soma + idade
    
    if sexo in 'M' and idade < 20:
        cont += 1
    
    elif sexo in 'H' and velho_idade < idade :
        velho = nome
        velho_idade = idade
        
        
media = soma / 4

print()
print(f'A média de idade do grupo é {media}.')
print(f'O homem mais velho do grupo é {velho}.')
print(f'Existe(m) {cont} mulher(es) com menos de 20 anos neste grupo.')