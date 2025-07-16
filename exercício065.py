# -*- coding: utf-8 -*-
"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média 
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao 
usuário se ele quer ou não continuar a digitar valores.
"""

print()

cont = soma = maior = menor = 0
pergunta = 'S'

while pergunta in 'Ss':
    n = int(input("Digite um número inteiro: "))
    print()
    
    pergunta = str(input("Você quer continuar digitando(S/N)? ")).upper().strip()
    soma += n
    cont += 1
    
    if cont == 1: 
        menor = maior = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
        
media = soma / cont

print()

print("A media entre todos os valores digitados é: {}". format(media))

print()
print("O menor número é {}.". format(menor))
print()
print("O maior número é {}.". format(maior))
print('Acabou.')
