# -*- coding: utf-8 -*-
"""
Crie um programa onde o usuário digite uma expressão qualquer que usa parênteses. Seu aplicativo deverá analisar 
se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

print('=' * 50 )

exp = str(input("Digite uma expressão: "))
print()

pilha = []

for simbolo in exp:
    if simbolo == '(':
        pilha.append(simbolo)
        
    elif simbolo == ')':
        pilha.append(simbolo)
        
if pilha.count('(') == pilha.count(')'):
    print('A expressão está correta.')

else:
    print('A expressão está incorreta.')

print('=' * 50 )

