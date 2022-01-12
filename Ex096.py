print(f'{" DESAFIO 096 ":=^60}')
def área(l, c):
    a = l*c
    print(f'A área de um terreno {l} x {c} é de {a:.2f} m²')


#Programa principal
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))
área(lar, com)
