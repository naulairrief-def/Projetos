# -*- coding: utf-8 -*-
"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000.
c) Qual é o nome do produto mais barato.
    
"""
print()

total = produto = menor = cont = 0
pergunta = 'S'

while pergunta == 'S':
    nome = str(input("Qual é o nome do produto? "))
    preco = float(input("Qual é o preço do produto? "))
    total += preco 
    cont += 1
    
    if cont == 1:
        menor = preco
        barato = nome
    else:
        menor = preco
        barato = nome
    if preco > 1000:
        produto += 1

        
    pergunta = str(input("Quer continuar?[S/N] ")).upper().strip()
    if pergunta == 'N':
        break
    print()

print()
print(f"O total pago pelos produtos é de R${total}.")
print(f"{produto} produto(s) custa(m) mais de R$1000.")
print(f"O nome do produto mais barato é {barato}.")


