# -*- coding: utf-8 -*-
"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que 
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

print()

valores = [[], []]
for i in range(1,8):
    
    n = int(input(f"Digite o {i}° valor: "))
    #valores.append(n)
    
    if n % 2 == 0:
        valores[0].append(n)
        
    else:

        valores[1].append(n)

valores[0].sort()
valores[1].sort()     
print()


print('Os números pares são: ', end='')
print(valores[0])
print()
print('Os números impares são: ', end='')
print(valores[1])
