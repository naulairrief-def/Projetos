# -*- coding: utf-8 -*-
"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
print()

from random import randint

print()

vitoria = 0

while True:
    n1 = int(input("Digite um número inteiro positivo: "))
    j_pergunta = str(input("P/I? ")).upper().strip()
    pc = randint(1, 100)
    soma = n1 + pc
    print()
    if soma % 2 == 0 and j_pergunta == 'P':
        print("O jogador ganhou.")
        vitoria += 1
        print()
        
    elif soma % 2 != 0 and j_pergunta == 'I':
        print("O jogador ganhou.")
        vitoria += 1
        print()
        
    elif soma % 2 != 0 and j_pergunta == 'P':
        print("O computador ganhou.")
        break  
    elif soma % 2 == 0 and j_pergunta == 'I':
        print("O computador ganhou.")
        break

print()
print(f"O jogador conseguiu {vitoria} vitória(s).")