# -*- coding: utf-8 -*-
"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.
"""
print()

from time import sleep

for número in range(10, 0, -1):
    print(número)
    sleep(1)