print(f'{" DESAFIO 095 ":=^60}')
dados = dict()
gols = list()
totjogadores = list()
while True:
    dados['nome'] = str(input('NOME DO JOGADOR: '))
    partidas = int(input(f'QUANTIDADE DE PARTIDAS DE {dados["nome"].upper()}: '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'\tQUANTIDADE DE GOLS NA PARTIDA {c}: ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    gols.clear()
    totjogadores.append(dados.copy())
    resp = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    if resp in 'Nn':
        break
print('=-'*30)
print(f'{"CÓD.":<7}{"NOME":<15}{"GOLS":<15}{"TOTAL":<3}')
print('-'*60)
for i, e in enumerate(totjogadores):
    print(f'{i:<7}{e["nome"]:<15}{str(e["gols"]):<15}{e["total"]:<3}')
while True:
    jogador = int(input('Mostrar dado de qual jogador? (999 para parar) '))
    if jogador == 999:
        break
    elif jogador >= len(totjogadores) or jogador < 0:
        print(f'ERRO! Não existe jogador com código {jogador}')
    else:
        print(f'→Levantamento do jogador {totjogadores[jogador]["nome"]}')
        for i, e in enumerate(totjogadores[jogador]['gols']):
            print(f'\tNo jogo {i+1}, {totjogadores[jogador]["nome"]} fez {e} gol(s)')
print(f'{"<<< PROGRAMA ENCERRADO >>>":^60}')