# -*- coding: utf-8 -*-
"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
de acordo com a idade:
    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 19 anos: JUNIOR
    - Até 20 anos: SENIOR 
    - Acima: MASTER
"""

print()
nome = input("Digite o nome do(a) atleta: ")
nasc = int(input("Em que ano o(a) atleta nasceu? "))

idade = 2024 - nasc

if idade < 9:
    print("MIRIM")

elif 9 <= idade < 14:
    print("INFANTIL")

elif 14 <= idade < 19:
    print("JUNIOR")
    
elif idade == 19 or idade == 20:
    print("SENIOR")

elif idade > 20:
    print("MASTER")
