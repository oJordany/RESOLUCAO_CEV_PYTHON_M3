print(f'{" DESAFIO 078 ":=^60}')
valores = list()
for c in range(0,5):
    valores.append(int(input(f'Digite o valor na posição {c}: ')))
print(f'Valores digitados: {valores}')
print(f'O maior valor digitado foi o {max(valores)} na(s) posição/posições: ',end = '')
print(valores.index(max(valores)), end = '...')
ultposmaior = valores.index(max(valores))
while True:
    if max(valores) in valores[ultposmaior+1:]:
        print(valores.index(max(valores), ultposmaior+1), end='...')
        ultposmaior = valores.index(max(valores), ultposmaior+1)
    else:
        break
print(f'\nO menor valor digitado foi o {min(valores)} na(s) posição/posições: ',end = '')
print(valores.index(min(valores)), end = '...')
ultposmaior = valores.index(min(valores))
while True:
    if min(valores) in valores[ultposmaior+1:]:
        print(valores.index(min(valores), ultposmaior+1), end='...')
        ultposmaior = valores.index(min(valores), ultposmaior+1)
    else:
        break
