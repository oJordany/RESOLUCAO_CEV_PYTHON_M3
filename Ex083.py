print(f'{" DESAFIO 083 ":=^60}')
exp = str(input('Digite a sua expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão VÁLIDA!')
else:
    print('Expressão INVÁLIDA!')
