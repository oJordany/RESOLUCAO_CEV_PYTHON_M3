from time import sleep
from random import sample
print(f'{" DESAFIO 088 ":=^60}')
print('-'*60)
print(f'{"JOGA NA MEGA SENA":^60}')
print('-'*60)
qntdjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*9,f' SORTEANDO {qntdjogos} JOGOS ','-='*10)
jogo = list()
totjogos = list()
for c in range(0,qntdjogos):
    jogo.append(sample(range(1,60),6))
    totjogos += jogo[:]
    jogo.clear()
    print(f'Jogo {c+1}: {totjogos[c]}')
    sleep(1)