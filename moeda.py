def aumentar(p = 0, a = 0, f = False):
    if f == True:
        return moeda(p + (p*a/100))
    else:
        return p + (p * a / 100)
def diminuir(p = 0, d = 0, f = False):
    if f == True:
        return moeda(p - (p*d/100))
    else:
        return p - (p*d/100)
def dobro(p = 0, f = False):
    if f == True:
        return moeda(p * 2)
    else:
        return p * 2
def metade(p = 0, f = False):
    if f == True:
        return moeda(p/2)
    else:
        return p/2
def moeda(p = 0):
    return f'R${p:.2f}'.replace('.', ',')
def resumo(p = 0, a = 10, d = 10):
    print('—'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('—' * 30)
    print(f'{"Preço analisado: ":<20}{moeda(p):<10}')
    print(f'{"Dobro do preço: ":<20}{dobro(p, True):<10}')
    print(f'{"Metade do preço: ":<20}{metade(p, True):<10}')
    print(f'{a:<3}%{" de aumento: ":<16}{aumentar(p, a,True):<10}')
    print(f'{d:<3}%{" de redução: ":<16}{diminuir(p, d, True):<10}')
    print('—' * 30)