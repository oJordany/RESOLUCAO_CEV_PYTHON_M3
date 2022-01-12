print(f'{" DESAFIO 105 ":=^60}')
def notas(*n, sit = False):
    """
    → Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas de vários alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    soma = 0
    for i, e in enumerate(n):
        soma += e
        if i == 0:
            maior = menor = e
        else:
            if e > maior:
                maior = e
            if e < menor:
                menor = e
    media = soma/len(n)
    if sit == False:
        inf = {'Total':len(n), 'Maior':maior, 'Menor':menor, 'Média':media}
        return inf
    else:
        if 5 <= media < 7:
            situacao = 'RAZOÁVEL'
        elif media < 5:
            situacao = 'RUIM'
        elif 7 <= media <= 8:
            situacao = 'BOA'
        else:
            situacao = 'EXCELENTE'
        inf = {'Total': len(n), 'Maior': maior, 'Menor': menor, 'Média': media, 'Situação': situacao}
        return inf


#Programa principal
resp = notas(4, 8, 10, 10, 9.5, 9)
print(resp)
help(notas)