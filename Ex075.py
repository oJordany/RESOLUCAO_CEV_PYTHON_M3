print('{:=^60}'.format(' DESAFIO 075 '))
tupla = ()
for t in range (1,5):
    acc = int(input(f'Insira o {t}º número: '))
    tupla += (acc,)
print(f'tupla: {tupla}')
verificador = bool(False)
print(f'O valor 9 apareceu {tupla.count(9)} vez(es)')
if 3 in tupla:
    print(f'O primeiro valor 3 foi digitado na posição {tupla.index(3) + 1}')
else:
    print(f'O valor 3 não foi digitado nenhuma vez')
verificador = bool(False)
for pos in range(0,4):
    if tupla[pos] % 2 == 0:
        verificador = True
if verificador == True:
    print('Os números pares foi/foram: ', end ='')
else:
    print('Não foram digitados números pares')
for pos,v in enumerate(tupla):
    if v % 2 == 0 and pos < 3:
        print(v, end = '\t')
    elif v % 2 == 0 and pos == 3:
        print(v)
