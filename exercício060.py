# -*- coding: utf-8 -*-
"""
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
#import math

print()

#n = int(input('Digite um número qualquer: '))

#fatorial = math.factorial(n)

print()

#print(f'{n}! é {fatorial}.')

n = int(input('Digite um número qualquer: '))

fatorial = 1
cont = n

while cont > 0:
    print(f'{cont}', end= '')
    print(' x ' if cont > 1 else ' = ', end= '')
    
    fatorial = fatorial * cont
    cont = cont - 1
    
print(fatorial)