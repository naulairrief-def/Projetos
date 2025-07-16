# -*- coding: utf-8 -*-
"""
Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da
estrutura na tela.
"""
print()
#pessoas = {'nome': 'Luan', 'sexo': 'M', 'idade': 26}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

#for k in pessoas.keys():
    #print(k)
#for p in pessoas.values():
    #print(p)
    
#for k, v, in pessoas.items():
    #print(f'{k} = {v}')
 
#pessoas['nome'] = 'Lucas'
#del pessoas['sexo']
#pessoas['peso'] = 89.3

#print(pessoas)
dic = dict()
dic['nome'] = str(input('Nome: '))
dic['media'] = float(input('Média: '))

print()

if dic['media'] < 5:
    print(f'O estudante {dic["nome"]} tem média {dic["media"]}, e por isso está reprovado.')
    
elif dic['media'] >= 5:
    print(f'O estudante {dic["nome"]} tem média {dic["media"]}, e por isso está aprovado.')

elif dic['media'] > 10:
    print('Essa média não existe!')