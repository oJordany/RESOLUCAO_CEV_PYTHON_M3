import moeda
print(f'{" DESAFIO 107 ":=^60}')
p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10)}')
print(f'Dimunuindo 13% temos {moeda.diminuir(p, 13)}')