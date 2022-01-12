from time import sleep
def contador(início, fim, passo):
    if passo == 0:
        passo = 1
    if início < fim:
        if passo < 0:
            passo *= -1
        for c in range(início, fim+1, passo):
            print(f'{c}  ', end='', flush=True)
            sleep(0.5)
    else:
        if passo > 0:
            passo *= -1
        for c in range(início, fim-1, passo):
            print(f'{c}  ', end='', flush=True)
            sleep(0.5)
    print('FIM!')
    print('-=' * 30)


#Programa principal
print('-='*30)
print('Contagem de 1 até 10 de 1 em 1')
contador(1,10,1)
print('Contagem de 10 até 0 de 2 em 2')
contador(10,0,-2)
print('Agora é a sua vez de realizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)