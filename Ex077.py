print('{:=^60}'.format(' DESAFIO 077 '))
tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
