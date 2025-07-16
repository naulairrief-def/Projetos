# -*- coding: utf-8 -*-
"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,desconsiderando os espaços.

Ex: 
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""
print()

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

print()

for letra in range(len(junto) - 1, -1, -1) : #estamos pegando a lista de traz para frente
    inverso += junto[letra] #adicionamos a letra obtida no recolhimento de trás para frente

if junto == inverso:
    print(f' A frase "{frase}" é um palíndromo!')
    
else:
    print(f'A frase "{frase}" não é um palíndromo!')
# print(junto, inverso)



