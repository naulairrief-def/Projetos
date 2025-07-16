# -*- coding: utf-8 -*-
"""
Melhore o desafio 061, perguntando ao usuário se ele quer mostrar mais alguns termos. O programa 
encerra quando ela disser que quer mostrar 0 termos.
"""

print()
a1 = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

cont = 1
termo = a1

while cont < 11:
    print(termo)
    
    termo += razao 
    cont += 1
    
p1 = int(input("Você quer mostrar mais quantos termos? ")) 

print()

if p1 == 0:
    print("Seu programa está encerrado.")
            
else:
    cont2 = 1
    n_termo = termo
        
    while cont2 <= p1:
        print(n_termo)
        
        n_termo += razao
        cont2 += 1
        
        #print(n_termo)
        #primeiro adiciona o termo e depois imprime, por isso podemos colocar o print(n_termo) antes de n_termo += razao.
            
            
            
            
    