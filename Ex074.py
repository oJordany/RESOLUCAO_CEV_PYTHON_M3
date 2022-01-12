from random import randint
print('{:=^60}'.format(' DESAFIO 074 '))
tupla = ()
for c in range (0,5):
    tupla += (randint(0,100),)
print(f'Números gerados: ', end = '')
for n in tupla:
    print(f'{n}', end = '  ')
print(f'\nO maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')
