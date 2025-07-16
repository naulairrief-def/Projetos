# -*- coding: utf-8 -*-
"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
programa será interrompido quando o número solicitado for negativo.
"""
print()


while True:
    numero = int(input("Quer ver a tabuada de número? "))
    print()
    if numero >= 0:
        for i in range(0, 11):
            resultado = i * numero
            print(f"{i} x {numero} = {resultado}")
            
    else:
        print("O número que você digitou é um inteiro menor do que 0.")
        break
    print()