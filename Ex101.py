print(f'{" DESAFIO 101 ":=^60}')
def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if 18 <= idade <= 65 :
        return f'Com {date.today().year - nasc} anos: VOTO OBRIGATÓRIO'
    elif idade == 16 or idade == 17 or idade > 65:
        return f'Com {date.today().year - nasc} anos: VOTO OPCIONAL'
    else:
        return f'Com {date.today().year - nasc} anos: NÃO VOTA'

#Programa principal
an = int(input('Digite o seu ANO DE NASCIMENTO: '))
print(voto(an))