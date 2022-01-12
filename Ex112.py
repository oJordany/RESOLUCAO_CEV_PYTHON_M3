print(f'{" DESAFIO 112 ":=^60}')
from utilidadesCeV import dado, moeda
p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)