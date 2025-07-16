# -*- coding: utf-8 -*-
"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram 
no intervalo de 1 até 500.
"""
print()
from time import sleep
print("OS NÚMEROS MÚLTIPLOS DE 3 QUE ESTÃO ENTRE 1 A 500 SÃO:")
sleep(1)

for n in range(1, 501):
    if n % 3 == 0:
       print(n, end= ' ')
       sleep(1)
