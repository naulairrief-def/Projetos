# -*- coding: utf-8 -*-
"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos 
de uma seq de fibonacci.
Ex: 0 1 1 2 3 5 8 
"""

print()

n = int(input("Digite um número inteiro positivo qualquer: "))

anterior = 0
atual = 1
soma = 0
cont = 0

print()

while cont < n:
    print(soma)
    anterior = atual
    atual = soma
    soma = anterior + atual
    cont += 1
    
    
    


    