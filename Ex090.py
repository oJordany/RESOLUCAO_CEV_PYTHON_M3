print(f'{" DESAFIO 090 ":=^60}')
infor = dict()
infor['Nome'] = str(input('Nome: '))
infor['Média'] = float(input(f'Média de {infor["Nome"]}: '))
print('-='*30)
if infor['Média'] >= 7:
    infor['Situação'] = 'Aprovado'
elif 5 <= infor['Média'] < 7:
    infor['Situação'] = 'Recuperação'
else:
    infor['Situação'] = 'Reprovado'
for k, v in infor.items():
    print(f'→{k} é igual a {v}')
