from time import sleep
from random import randint
print(f'{" DESAFIO 088 ":=^60}')
print('-'*60)
print(f'{"JOGA NA MEGA SENA":^60}')
print('-'*60)
qntdjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*9,f' SORTEANDO {qntdjogos} JOGOS ','-='*10)
jogo = list()
totjogos = list()
for c in range(0,qntdjogos):
    cont = 1
    while cont <= 6:
        jogo.append(randint(1,60))
        if jogo[-1] in jogo[0:-1]:
            jogo.pop()
            cont -= 1
        cont += 1
    totjogos += [jogo[:]]
    jogo.clear()
    print(f'Jogo {c+1}: {totjogos[c]}')
    sleep(1)
print('-='*5, ' BOA SORTE! ', '-='*5)