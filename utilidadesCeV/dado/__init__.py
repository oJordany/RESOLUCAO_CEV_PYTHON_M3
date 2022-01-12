def leiaDinheiro(msg):
    while True:
        p = str(input(msg))
        aux = p.strip()
        if ',' in aux:
            aux = aux.replace(',', '.')
        ver = aux.replace('.', '')
        if ver.isnumeric() == True:
            aux = float(aux)
            break
        else:
            print(f'\033[1;31mERRO: \"{p}\" não é um preço válido!\033[m')
    return aux