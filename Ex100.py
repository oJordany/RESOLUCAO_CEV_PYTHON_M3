from random import randint
from time import sleep
def sorteia(lst):
    for c in range(0,5):
        lst.append(randint(0, 100))
    print('Sorteando 5 valores: ',end='')
    for e in lst:
        print(e, end=' ')
        sleep(0.5)
    print('PRONTO!')


def somapar(lst):
    soma = 0
    for e in lst:
        if e%2 == 0:
            soma += e
    print(f'Somando os valores pares de {lst}, temos {soma}')


#Programa principal
print(f'{" DESAFIO 100 ":=^60}')
lista = list()
sorteia(lista)
somapar(lista)
