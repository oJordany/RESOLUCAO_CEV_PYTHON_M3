print(f'{" DESAFIO 104 ":=^60}')
def leiaInt():
    while True:
        n = input('Digite um número: ')
        if not n.isnumeric() or n == '':
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return n


#Programa principal
n = leiaInt()
print(f'Você acabou de digitar o número {n}')