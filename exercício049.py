# -*- coding: utf-8 -*-
"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""
print()
print('-' * 40)

n = int(input("Digite um número inteiro: "))
print('-' * 40)

for i in range(11):
    print(' {} x {} = {}'. format(n, i,n * i))
    
   
#lista = [i for i in range(11)]
#print(lista)