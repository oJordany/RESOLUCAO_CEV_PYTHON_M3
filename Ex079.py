print(f'{" DESAFIO 079 ":=^60}')
lista = [int(input('Digite um valor inteiro: '))]
print('Número cadastrado COM SUCESSO!')
res = str(input('Você quer cadastrar outro número? [S/N]: '))[0]
while res in 'Ss':
    lista.append(int(input('Digite outro valor inteiro: ')))
    if lista[-1] in lista[:-1]:
        print('Número duplicado. Cadastro SEM SUCESSO')
        lista.pop()
    else:
        print('Número cadastrado COM SUCESSO!')
    res = str(input('Você quer cadastrar outro número? [S/N]: '))[0]
lista.sort()
print(f'Os valores cadastrados (em ordem crescente) foram: {lista}')