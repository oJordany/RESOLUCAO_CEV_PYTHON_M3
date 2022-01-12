print(f'{" DESAFIO 087 ":=^40}')
matriz = [[],[],[]]
somavpares = 0
somav3c = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite uma valor para a posição [{l},{c}]: ')))
        if matriz[l][-1] % 2 == 0:
            somavpares += matriz[l][-1]
print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        if c < 2:
            print(f'[{matriz[l][c]:^7}]', end='  ')
        else:
            print(f'[{matriz[l][c]:^7}]')
            somav3c += matriz[l][c]
print('-='*20)
print(f'A soma dos valores pares digitados é: {somavpares}')
print(f'A soma dos valores da 3ª coluna é: {somav3c}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')


