# -*- coding: utf-8 -*-
"""
Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
    
a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos.
"""

print()

maior_idade = homem = mulher = 0
pergunta = 'S'

while pergunta == 'S':
    idade = int(input("Qual é a idade da pessoa? ")) 
    sexo = str(input("Qual é o sexo da pessoa?[M/F] ")).upper().strip()
 
    if pergunta == 'N':
        break

    elif idade > 18 and sexo == 'M':
        maior_idade += 1
        homem += 1
        
    elif idade < 20 and sexo == 'F':
        mulher += 1
        
    elif idade > 18:
        maior_idade += 1
        
    pergunta = str(input("Quer registrar a idade e o sexo de mais pessoas? ")).upper().strip()
    print()

print()
print(f"Existe(m) ao todo {mulher} mulhere(s) com abaixo de 20 anos.")
print(f"Existe(m) ao todo {homem} homen(s) cadastrado(s).")
print(f"Existe(m) ao todo {maior_idade} pessoa(s) com mais de 18 anos.")

#na próxima vez, deixar o break no final do laço.







