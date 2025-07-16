# -*- coding: utf-8 -*-
"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão 
contar apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas.
"""

print()

valores = []

for i in range(0, 10):
    num = int(input("Digite um valor: "))
    valores.append(num)
    par = []
    impar = []
    for n in valores:

        if n % 2 == 0:
            par.append(n)
    
        else:
            impar.append(n)
print()
print(valores)
print()
print(par)
print()
print(impar)













