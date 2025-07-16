# -*- coding: utf-8 -*-
"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição 
correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
print()

val = []

for i in range(0, 5):
    n = int(input("Digite um valor: "))
    
    if i == 0:
        val.append(n)
        
    elif n > val[-1]:
        val.append(n)
    
    else:
        pos = 0
        while pos < len(val):
             if n <= val[pos]:
                 val.insert(pos, n)
                 break
             pos += 1
    

print(val)


#tentar entender depois






