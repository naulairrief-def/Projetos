# -*- coding: utf-8 -*-
"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
print()

n = (int(input("Digite o primeiro valor: ")),
      int(input("Digite o segundo valor: ")),
      int(input("Digite o terceiro valor: ")),
      int(input("Digite o quarto valor: ")))

print()


nove = n.count(9)
print(f'O número 9 aparece {nove} vez(es).' )
print()


if 3 in n:
    pos = n.index(3) + 1
    print(f'O valor 3 foi adicionado primeiro na {pos}° posição.')
else:
    print('O número 3 não aparece nenhuma vez.')
print()

print('Os números pares são:', end=' ')
for n in n:
    if n % 2 == 0:
        print(n, end=' ')