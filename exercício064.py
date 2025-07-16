# -*- coding: utf-8 -*-
"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o 
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles(desconsiderando a flag).
"""

print()

cont = 0
soma = 0
while True: 
    numero = int(input("Digite um número inteiro positivo: "))
    if numero == 999:
        break
    else: 
        cont += 1
        soma += numero

print()
print("Foram digitados {} números.". format(cont))
print()
print("A soma de todos os números digitados resulta em {}.".format(soma))








