# -*- coding: utf-8 -*-
"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    - Equilátero: todos os lados iguais.
    - Isósceles: dois lados iguais.
    - Escaleno: todos os lados diferentes
"""

print()
reta1 = float(input("Qual é o comprimento da dessa reta? "))
reta2 = float(input("Qual é o comprimento da dessa reta? "))
reta3 = float(input("Qual é o comprimento da dessa reta? "))

print()
if reta1 + reta2 >= reta3 and reta1 + reta3 >= reta2 and reta2 + reta3 >= reta1:
    if reta1 == reta2 == reta3:
        print("As retas com medidas {}, {} e {} formam um triângulo Equilátero.". format({reta1}, {reta2}, {reta3}))
        print()
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("As retas com medidas {}, {} e {} formam um triângulo Isósceles.". format({reta1}, {reta2}, {reta3}))
        print()
    else:
        print("As retas com medidas {}, {} e {} formam um triângulo Escaleno.". format({reta1}, {reta2}, {reta3}))
else:
    print("As retas com medidas {}, {} e {} não podem formar um triângulo.". format({reta1}, {reta2}, {reta3}))