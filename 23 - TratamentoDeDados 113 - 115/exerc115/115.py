from agenda.opcoes import *
from agenda.arquivo import *

arq = 'cev.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)



while True:
    respos = menu(['Mostrar cadastros', 'Novo cadastro', 'Sair'])
    if respos == 1:
        cabecalho("PESSOAS CADASTRADAS")
        lerArquivo(arq)
    elif respos == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif respos == 3:
        cabecalho('Encerrando sistema')
        break
    else:
        print("Opção invalida. Tente novamente")
        print(linha())
