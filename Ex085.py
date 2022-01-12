print(f'{ "DESAFIO 085 ":=^60}')
valores = [[],[]]
for c in range(0,7):
    val = int(input(f'Digite o {c+1}º valor inteiro: '))
    if val % 2 == 0:
        valores[0].append(val)
    else:
        valores[1].append(val)
valores[0].sort()
valores[1].sort()
totval = valores[0] + valores[1]
totval.sort()
print('-='*30)
print(f'Total de valores digitados: {totval}')
print(f'Valores pares digitados: {valores[0]}')
print(f'Valores ímpares digitados: {valores[1]}')