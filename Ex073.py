print('{:=^60}'.format(' DESAFIO 073 '))
tabela = ('Atlético-MG','Palmeiras','Flamengo','Fortaleza','Bragantino','Corinthians','Internacional','Fluminense','Cuiabá','Atlético-PR',
          'Atlético-GO','São Paulo','Ceará SC','Santos','Bahia','América-MG','Juventude','Grêmio','Sport Recife','Chapecoense')
print(f'Tabela 20 primeiros colocados: {tabela}')
print('=-'*138)
print(f'Cinco primeiros colocados: {tabela[:5]}')
print('=-'*138)
print(f'Últimos 4 colocados: {tabela[-4:]}')
print('=-'*138)
print(f'Lista em ordem alfabética: {sorted(tabela)}')
print('=-'*138)
print(f'A Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição')