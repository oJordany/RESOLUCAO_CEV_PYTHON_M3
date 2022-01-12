import datetime
print(f'{" DESAFIO 092 ":=^60}')
dados = dict()
dados['Nome'] = str(input('NOME: '))
nasc = int(input('ANO DE NASCIMENTO: '))
dados['CTPS'] = int(input('CARTEIRA DE TRABALHO (0 não tem): '))
dados['Idade'] = datetime.date.today().year - nasc
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
    dados['Salário'] = float(input('SALÁRIO: R$'))
    dados['Aposetandoria'] = 35 + (dados['Contratação'] - nasc)
print('-='*30)
for k, v in dados.items():
    print(f'\t— {k} tem o valor {v}')
