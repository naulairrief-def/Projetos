# -*- coding: utf-8 -*-
"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
    - À vista dinheiro/ cheque: 10% de desconto
    - À vista no cartão: 5% de desconto
    - Em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros
"""
print()
preco = float(input("Quanto custa o produto?: "))
pag = str(input("Qual é a forma de pagamento?? "))

if pag == "À vista dinheiro/cheque":
    print(0.9*preco)
    
elif pag == "À vista no cartão":
    print(0.95*preco)
    
elif pag == "Em até 2x no cartão":
    print(preco)
    
elif pag == "#x ou mais no cartão":
    print(1.2*preco)