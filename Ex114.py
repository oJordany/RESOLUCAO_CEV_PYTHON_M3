import urllib
import urllib.request
print(f'{" DESAFIO 114 ":=^60}')
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mERRO! Não é possível acessar o site pudim.com.br\033[m')
else:
    print('\033[32mO site pudim.com.br foi acessado com sucesso\033[m')
    print(site.read())

