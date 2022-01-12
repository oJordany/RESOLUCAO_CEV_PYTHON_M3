print(f'{" DESAFIO 082 ":=^60}')
valores = []
valorespar = []
valoresimpar = []
while True:
    valores.append(int(input('Digite um valor inteiro: ')))
    res = str(input('Você quer digitar mais números? [S/N]: '))[0]
    if res in 'Nn':
        break
for valor in valores:
    if valor % 2 == 0:
        valorespar.append(valor)
    else:
        valoresimpar.append(valor)
print(f'LISTA DE TODOS OS VALORES DIGITADOS: {valores}')
print(f'LISTA DOS VALORES PARES DIGITADOS: {valorespar}')
print(f'LISTA DE TODOS OS VALORES ÍMPARES DIGITADOS: {valoresimpar}')
        