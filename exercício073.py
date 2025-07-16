# -*- coding: utf-8 -*-
"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de 
colocação. Depois mostre:

a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com times em ordem alfabética.
d) Em que posição na tabela está o time do Bragantino.
"""

tabela = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'Sao Paulo', 'Corinthians', 'Bahia', 'Cruzeiro',
          'Vasco da Gama', 'Vitoria', 'Atletico Mineiro', 'Fluminense', 'Gremio', 'Juventude', 'Bragantino', 'Atletico PR',
          'Criciuma', 'Atletico Goianiense', 'Cuiaba')

print('=' * 50)
print("{:^50}". format("TABELA DO CAMPEONATO BRASILEIRO"))
print('=' * 50)
print("{:^50}". format("CINCO PRIMEIROS COLOCADOS"))
print('=' * 50)

for time in range(0, 5):
    print(tabela[time])
print('=' * 50)
print("{:^50}". format("REBAIXADOS"))
print('=' * 50)

for time in range(16, 20 ):
    print(tabela[time])
print('=' * 50)

print("{:^50}". format("TIMES EM ORDEM ALFABÉTICA"))
print('=' * 50)
print(sorted(tabela))

print("=" * 50)

print("{:^50}". format("POSIÇÃO DO BRAGANTINO"))

pos = tabela.index('Bragantino')
print(f'O Bragantino está na {pos}° posição.')


