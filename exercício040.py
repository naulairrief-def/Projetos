# -*- coding: utf-8 -*-
"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
    - Média abaixo de 5.0: REPROVADO
    - Média entre 5.0 e 6.9: RECUPERAÇÃO
    - Média 7.0 ou superior: APROVADO
"""
print()
nome = str(input("Qual é o nome do(a) estudante?: "))
print()
nota1 = float(input("Qual é a primeira nota? "))
nota2 = float(input("Qual é a segunda nota? "))

media = (nota1 + nota2) / 2
print()
if media < 5:
    print("Olá {}, a sua media final foi {} e sendo assim, você está reprovado(a)!". format(nome, media))
    
elif media >= 5 and media < 7:
    print("Olá {}, a sua media final foi {} e sendo assim, você está de recuperação!". format(nome, media))

elif media >= 7:
    print("Olá {}, a sua media final foi {} e sendo assim, você está aprovado(a)!". format(nome, media))