print(f'{" DESAFIO 084 ":=^60}')
dados = list()
totdados = list()
pesmaispesada = list()
pesmaisleve = list()
maispesada = maisleve = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (Kg): ')))
    totdados.append(dados[:])
    dados.clear()
    res = str(input('Quer continuar? [S/N]: '))[0]
    if res in 'Nn':
        break
print(f'Foram cadastradas {len(totdados)} pessoas')
for pos, p in enumerate(totdados):
    if pos == 0:
        pesmaispesada.append(p[0])
        pesmaisleve.append(p[0])
        maispesada = maisleve = p[1]
    else:
        if p[1] < maisleve:
            maisleve = p[1]
            pesmaisleve.clear()
            pesmaisleve.append(p[0])
        elif p[1] == maisleve:
            pesmaisleve.append(p[0])
        if p[1] > maispesada:
            maispesada = p[1]
            pesmaispesada.clear()
            pesmaispesada.append(p[0])
        elif p[1] == maispesada:
            pesmaispesada.append(p[0])
print(f'O maior peso foi {maispesada} Kg. Peso de: {pesmaispesada}')
print(f'O menor peso foi {maisleve} Kg. Peso de: {pesmaisleve}')