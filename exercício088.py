# -*- coding: utf-8 -*-
"""
Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão 
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastranho em uma lista composta.
"""
print('-' * 40)
print('{:^40}'.format('JOGOS DA MEGA SENA'))
print('-' * 40)
from random import randint

lista = list()
jogos = list()
quant = int(input('Quantos jogos serão sorteados? '))

tot = 1
while tot <= quant:
    cont = 0    
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-' * 40)   
#print(f'Os números sorteados foram {jogos}')
print('-' * 40)     

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')



