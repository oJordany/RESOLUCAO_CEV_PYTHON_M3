from time import sleep
def maior(*nums):
    print('Analisando os valores passados...')
    if nums == ():
        Maior = 0
    else:
        for i, v in enumerate(nums):
            if i == 0:
                Maior = v
            elif v > Maior:
                Maior = v
            print(v, end=' ')
            sleep(0.5)
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {Maior}')
    print('-='*30)


#Programa principal
print(f'{" DESAFIO 099 ":=^60}')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()