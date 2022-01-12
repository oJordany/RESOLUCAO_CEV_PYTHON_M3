print(f'{" DESAFIO 094 ":=^60}')
dados = dict()
totdados = list()
somai = 0
mulheres = list()
Mqmedia = list()
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: '))
        if dados['sexo'] in 'MmFf':
            break
        print('ERRO! Por favor, responda apenas M ou F')
    dados['idade'] = int(input('Idade: '))
    somai += dados['idade']
    totdados.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: '))
        if resp in 'Nn':
            break
        elif resp in 'Ss':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp in 'Nn':
        break
print('-='*30)
print(f'A) Ao todo temos {len(totdados)} pessoas cadastradas.')
print(f'B) A média de idade é de {somai/len(totdados):.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for e in totdados:
    if e['sexo'] in 'Ff':
        print(e['nome'], end='  ')
print(f'\nD) Lista das pessoas que estão acima da média de idade: ')
for e in totdados:
    if e['idade'] > somai/len(totdados):
        print('\t\t', end='')
        for k, v in e.items():
            print(f'{k} = {v}; ',end='')
        print()
print('\t\t\t    <<< ENCERRADO >>>')
