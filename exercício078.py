# -*- coding: utf-8 -*-
"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e suas respectivas posições na lista.
"""
#num = [1,2,3,4,5,6,7]
#num.append(5)
#num.sort(reverse=True)

#num.pop(3)
#num.insert(3,8)
#num.append(10)
#num.append(11)
#num.append(7)

#b = num.copy()
#b.append(55)
#for cont in range(0, 6):
   #num.append(int(input('Digite um valor: ')))
#print()

#for c, v in enumerate(num):
    #print(f'Na posição {c} encontrei o valor {v}.')

#print('Fim da Lista.')

#print(b)

print()

lista = []

for n in range(0, 5):
    
    num = int(input("Digite um valor: "))

    lista.append(num)
    lista.sort()

maior = max(lista)
menor = min(lista)
print()
print(lista)
print()
print(f'O maior número digitado foi {maior}.')
print()
print(f'O menor número digitado foi {menor}.')






