print('{:=^60}'.format(' DESAFIO 076 '))
lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-'*60)
print('{:^60}'.format('LISTAGEM DE PREÇOS'))
print('-'*60)
for c in range(0,len(lista),2):
    print('{:.<52}R${:>6.2f}'.format(lista[c], lista[c+1]))
print('-'*60)
