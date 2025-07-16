# -*- coding: utf-8 -*-
"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
    - Abaixo de 18.5: Abaixo do Peso.
    - Entre 18.5 e 25: Peso Ideal.
    - 25 até 30: Sobrepeso.
    - 30 até 40: Obesidade.
    - Acima de 40: Obesidade mórbida
"""
    
nome = str(input("Qual é o nome da pessoa?: "))
peso = float(input("Qual é o peso da pessoa(em kg)?: "))
altura = float(input("Qual é a altura da pessoa(em m)?: "))
imc = peso / (altura * altura)
        
if imc < 18.5:
    print("Senhor(a) {}, você está abaixo do peso.".format(nome))
            
elif 18.5 <= imc < 25:
    print("Senhor(a) {}, você está dentro do peso.".format(nome))
        
elif 25 <= imc < 30:
    print("Senhor(a) {}, você está com sobrepeso.".format(nome))
            
elif 30 <= imc < 40:
    print("Senhor(a) {}, você está com obesidade.".format(nome))
            
elif 18.5 < imc < 25:
    print("Senhor(a) {}, você está com obesidade mórbida.".format(nome))

