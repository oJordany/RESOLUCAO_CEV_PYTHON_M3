print('{:=^60}'.format(' DESAFIO 072 '))
nextenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove', 'vinte')
res = 's'
while res in 'Ss':
    num = int(input('Digite um número entre 0 e 20: '))
    if num <= 20 and num >= 0:
        print(f'Você digitou o número: {nextenso[num]}')
        res = str(input('Você quer verificar outro número? [S/N]: '))[0]
    else:
        print('Tente novamente. ', end='')
