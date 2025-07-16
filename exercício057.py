# -*- coding: utf-8 -*-
"""
Facça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso
esteja errado. peça a digitação novamente até ter um valor correto.
"""
print()
nome = str(input("Digite seu nome: "))
sexo = str(input("Qual é o seu sexo?[F/M]: ")).strip().upper()[0]

print()

while sexo not in 'MF':
    print('Desculpe, não entendi, digite novamente. ')
    print()
    nome = str(input("Digite seu nome: "))
    sexo = str(input("Qual é o seu sexo?[F/M]: ")).upper()
    
print()

print(f'Olá, {nome}.')