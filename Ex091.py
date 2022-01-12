from random import randint
from time import sleep
from operator import itemgetter
print(f'{" DESAFIO 091 ":=^60}')
init = input('Aperte ENTER para iniciar o programa: ')
resultados = dict()
for c in range(1,5):
    resultados[f'jogador{c}'] = randint(1,6)
print('Valores Sorteados:')
ranking = list()
for k, v in resultados.items():
    print(f'\tO {k} tirou {v}')
    sleep(1)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse =True)
print('-='*30)
print('Ranking dos jogadores: ')
for i, v in enumerate(ranking):
    print(f'\t{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
