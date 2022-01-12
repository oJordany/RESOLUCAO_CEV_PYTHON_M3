print(f'{" DESAFIO 102 ":=^60}')
def fatorial(número, show = False):
    """
    → Calcula o Fatorial de um número
    :param número: O número a ser calculado
    :param show: (opcional) Mostrar ou não o processo de cálculo
    :return: O valor do fatorial de um número n
    """
    f = 1
    for c in range(número, 0, -1):
        f *= c
        if show == True:
            if c > 1:
                return print(f'{c} x', end=' ')
            else:
                return print(f'{c} = {f}')
    if show == False:
        return print(f'{número}! = {f}')


#Programa principal
n = int(input('Digite um número: '))
s = str(input(f'Você quer ver o processo de cálculo do fatorial de {n} ? [S/N] ')).strip().upper()[0]
if s == 'S':
    s = True
    fatorial(n, show=s)
else:
    fatorial(n)

