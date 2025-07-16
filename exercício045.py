# -*- coding: utf-8 -*-
"""
Crie um programa que faça o computador jogar JOKEMPÔ com você
"""
print()
from random import randint
jogador = int(input("Digite 1 para pedra, 2 para papel ou 3 tesoura: "))


pc = randint(1, 3)


if pc == 1 and jogador == 3:
    print("O pc escolheu pedra e o jogador escolheu tesoura, por isso o pc venceu!")
    
elif pc == 2 and jogador == 1:
    print("O pc escolheu tesoura e o jogador escolheu pedra, por isso o jogador venceu!")
    
elif pc == 3 and jogador == 2:
    print("O pc escolheu tesoura e o jogador escolheu papel, por isso o pc venceu!")
    
elif pc == 1 and jogador == 2:
    print("O pc escolheu tesoura e o jogador escolheu papel, por isso o jogador venceu!")

elif pc == 2 and jogador == 3:
    print("O pc escolheu tesoura e o jogador escolheu papel, por isso o jogador venceu!")

elif pc == 3 and jogador == 1:
    print("O pc escolheu tesoura e o jogador escolheu papel, por isso o jogador venceu!")
    
elif pc == 1 == jogador or pc == 2 == jogador or pc == 3 == jogador:
    print("Empate!")