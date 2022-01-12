print(f'{" DESAFIO 089 ":=^60}')
aluno = list()
notas = list()
totdados = list()
while True:
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    totdados += [aluno[:]]
    aluno.clear()
    notas.clear()
    res = str(input('Quer continuar? [S/N]: '))[0]
    if res in 'Nn':
        break
print('-='*30)
print('Nº     NOME          MÉDIA')
print('-'*26)
for n, c in enumerate(totdados):
    media = (c[1][0] + c[1][1]) / 2
    print(f'{n:<7}{c[0]:<15}{media:>.1f}')
print('-'*26)
while True:
    naluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if naluno == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    print(f'Notas de {totdados[naluno][0]}: {totdados[naluno][1]}')
    print('-'*60)
