print(f'{"DESAFIO 081 ":=^60}')
lista = []
while True:
    lista.append(int(input('Digite um valor inteiro: ')))
    res = str(input('Você quer digitar outro número? [S/N]: '))[0]
    if res in 'Nn':
        break
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse = True)
print(f'Lista dos valores em ordem decrescente: {lista}')
if 5 in lista:
    print(f'Foi/Foram digitado(s) {lista.count(5)} número(s) 5')
else:
    print('O número 5 não foi digitado nenhuma vez')