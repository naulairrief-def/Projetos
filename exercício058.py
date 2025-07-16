# -*- coding: utf-8 -*-
"""
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram 
necessários para vencer.
"""

print()
import random

numero = int(input("Digite um número inteiro entre 0 e 5: "))

sorteado = random.randint(0, 10)
print()

while numero != sorteado:
    numero = int(input("Digite um número inteiro entre 0 e 5: "))
    print()
    
print(f'Parabéns, o número que o pc escolheu foi {sorteado} e você acertou!')

    
