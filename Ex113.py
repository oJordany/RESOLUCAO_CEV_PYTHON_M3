print(f'{" DESAFIO 116 ":=^60}')
def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


#Programa principal
n = leiaInt()
print(f'Você acabou de digitar o número inteiro {n}')
f = leiaFloat()
print(f'Você acabou de digitar o número decimal {f}')