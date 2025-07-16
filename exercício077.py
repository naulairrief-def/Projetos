# -*- coding: utf-8 -*-
"""
Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para 
cada palavra, quais são as suas vogais.
"""
print()
palavras = ('Um', 'dia', 'eu', 'vou', 'dominar', 'o', 'mundo')
#print(palavras)
vogal = 0
print()

for p in palavras:
    print()
    print(f'\nNa palavra {p} temos as vogais:', end=' ')
    for letra in p:
        if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
            print(letra, end=' ')



#\n quebra a linha.