from Ex115.lib.interface import *
from Ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o contúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = str(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do Sistema.
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)