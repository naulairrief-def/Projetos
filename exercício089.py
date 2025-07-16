# -*- coding: utf-8 -*-
"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
"""

print()

aluno = list()
print('{:^50}'.format('BOLETIM DE NOTAS'))
while True:
    print()
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    
    aluno.append([nome, [nota1, nota2], media])
    #print(f'Primeira nota: {nota1:.2f}')
    #print(f'Segunda nota: {nota2:.2f}')
    #print(f'A média de notas do estudante {nome} é {media:.2f}.')
    print()
    p = str(input('Quer continuar?[S/N]: ')).strip().upper()
    if p in 'Nn':
        break
print()
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":<8}')
print('-' * 26)
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print()
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 encerra): '))
    if opc == 999:
        break
    if opc <= len(aluno) - 1:
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')
        
print('ACABOU!')
        
