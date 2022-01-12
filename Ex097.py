print(f'{" DESAFIO 097 ":=^60}')
def escreva(msg):
    tam = len(msg) + 6
    print('~'*tam)
    print(f'   {msg}')
    print('~' * tam)

#Programa principal
while True:
    msg = str(input('Insira a sua mensagem: '))
    escreva(msg)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
