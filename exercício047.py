# -*- coding: utf-8 -*-
"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
print()
from time import sleep
print("OS NÚMEROS PARES DE 1 A 50 SÃO:")
sleep(1)
for número in range(1,51):
    if número % 2 == 0:
        print(número, end= " ")
        sleep(1)
        