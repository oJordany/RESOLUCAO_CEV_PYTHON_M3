print(f'{" DESAFIO 086 ":=^40}')
matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite uma valor para a posição [{l},{c}]: ')))
print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^7}]', end='  ')
    print()