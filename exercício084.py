# -*- coding: utf-8 -*-
"""
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

#teste = list()
#teste.append('Luan')
#teste.append('26')
#galera = list()
#alera.append(teste[:])
#teste[0] = 'Eike'
#teste[1] = 28
#galera.append(teste[:])
#print(galera[0][0])

#galera = list()
#dado = list()
#totmai = totmen = 0
#for c in range(0, 3):
   #dado.append(str(input('Nome: ')))
   #dado.append(int(input('Idade: ')))
   #galera.append(dado[:])
   #dado.clear()

#for p in galera:
   #if p[1] >= 21:
       #print(f'{p[0]} é maior de idade.')
       #totmai += 1
   #else:
       #print(f'{p[0]} é menor de idade.')
       #totmen += 1
        
#print(f'Temos {totmai} maiores e {totmen} menores de idade.')
#pergunta = ''

t = list()
c =  []

pessoas = 1
maior = menor = 0
print()
while True:
    
    t.append(str(input("Digite um nome: ")))
    t.append(float(input("Digite um peso em kg: "))) 
    c.append(t[:])
    if len(t) == 0:
        maior = menor = t[1]
    else:
        if t[1] > maior:
            maior = t[1]
    
        if t[1] < menor:
            menor = t[1]
    t.clear()         
    pergunta = str(input("Quer continuar? [S/N]: "))
    print()
    
    if pergunta in 'Nn':
        break

    pessoas += 1
        
        
print(f'{pessoas} pessoas tiveram as suas informações registradas.')
print()
print(f'O maior peso foi de {maior}kg', end='')
print()

for p in c:
    if p[1] == maior:
        print(f'A pessoa que pesa mais é {p[0]}.')

print()
print(f'O menor peso foi de {menor}kg', end='')

for p in c:
    if p[1] == menor:
        print()
