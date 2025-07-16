# -*- coding: utf-8 -*-
"""
Crie um programa que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
print()

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print()

opcao = 0

while opcao != 5:
    print('''       [1] somar
             [2] multiplicar
             [3] maior
             [4] novos números
             [5] sair do programa''')
    
    print()
    opcao = int(input('Qual é a sua opção? '))
    print()
    if opcao == 1:
        print(f'A soma de {n1} com {n2} é ', n1 + n2)
    
    elif opcao == 2:
        print(f'A multiplicação de {n1} por {n2} é ', n1 * n2)
    
    elif opcao == 3:
        print(f'O maior número entre {n1} e {n2} é', max(n1, n2))
    
    elif opcao == 4:
        print('Novos Números')
        print()
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    
    elif opcao == 5:
        break
    else:
        print('Opção inválida. Tente novamente.')

print()
print('Fim do programa.')