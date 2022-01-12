print(f'{" DESAFIO 093 ":=^60}')
dados = dict()
gols = list()
dados['nome'] = str(input('NOME DO JOGADOR: '))
partidas = int(input(f'QUANTIDADE DE PARTIDAS DE {dados["nome"].upper()}: '))
for c in range(1, partidas + 1):
    gols.append(int(input(f'\tQUANTIDADE DE GOLS NA PARTIDA {c}: ')))
dados['gols'] = gols.copy()
dados['total'] = sum(gols)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, e in enumerate(gols):
    print(f'\t→ Na partida {i}, {dados["nome"]} fez {e} gol(s)')
print(f'Foi um total de {dados["total"]} gols')
