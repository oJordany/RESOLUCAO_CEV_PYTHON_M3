print(f'{" DESAFIO 103 ":=^60}')
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


#Programa principal
n = str(input('Nome do jogador: '))
g = str(input(f'Quantidade de gols de {n}: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)
