print(f'{" DESAFIO 106 ":=^60}')
def titulo1(msg, tam):
    print('\033[1;30;46m~'*(tam))
    print(f'{msg}')
    print('\033[1;30;46m~' * (tam))
    print('\033[m',end='')


def titulo2(msg, tam):
    print('\033[1;30;45m~'*(tam))
    print(f'{msg}')
    print('\033[1;30;45m~' * (tam))
    print('\033[m',end='')


def titulo3(msg, tam):
    print('\033[1;30;41m~'*(tam))
    print(f'{msg}')
    print('\033[1;30;41m~' * (tam))
    print('\033[m',end='')


def manual(comando):
    print('\033[34m')
    help(comando)
    print('\033[m', end='')

    
#Programa principal
while True:
    msg = '   SISTEMA DE AJUDA PyHELP'
    titulo2(msg, len(msg)+3)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        msg = '   ATÉ LOGO'
        titulo3(msg, len(msg)+3)
        break
    msg = f'   Acessando o manual do comando {comando}'
    titulo1(msg, len(msg)+3)
    manual(comando)
