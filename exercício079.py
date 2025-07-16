# -*- coding: utf-8 -*-
"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos 
digitados, em ordem crescente.
"""

print()

valores = []

for i in range(0,10):
    n = int(input("Digite um valor: "))
    if n in valores:
        print()
        print(f'O número {n} já consta a lista.')
        print()
    else:
        valores.append(n)
    #valores.append(n)
    
for i in range(0,5):
    n = int(input("Digite um valor: "))     
    if n in valores:
        print()
        print(f'O número {n} já consta a lista.')
        print()
    else:
        valores.append(n)
        
valores.sort()
print()
print(f'Os valores registrados, em ordem crescente, são {valores}.')