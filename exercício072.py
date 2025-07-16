# -*- coding: utf-8 -*-
"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
"""

print()

contagem = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
            'quatorze', 'quinte', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

#print(contagem)
num = int(input("Digite um número natural entre 0 e 20: "))
print()

for n in contagem:
    if num == contagem.index(n) + 1:
        print(f'O número {num} escrito por extenso é {n}.' )
        
#print(contagem.index(n))