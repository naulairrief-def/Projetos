# -*- coding: utf-8 -*-
"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de 
números gerados e também indique o menor e o maior valor que estão na tupla.
"""

import random 

n1 = random.randint(0, 1000)
n2 = random.randint(0, 1000)
n3 = random.randint(0, 1000)
n4 = random.randint(0, 1000)
n5 = random.randint(0, 1000)

val = (n1, n2, n3, n4)

maior = max(val)
menor = min(val)

print(f'O maior valor registrado foi {maior}.')
print(f'O menor valor registrado foi {menor}.')

