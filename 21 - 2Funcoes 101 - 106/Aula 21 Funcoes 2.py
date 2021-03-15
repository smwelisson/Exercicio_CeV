# def mostraLinha(frase):
#     '''Criar um cabeçalho com o parametro passado
#     :param frase: Frase para o cabeçalho
#     :return: sem retorno'''
#     print("-" * 30)
#     print(frase)
#     print("-" * 30)
#
# # mostraLinha("Sistema de alunos")
# # print(mostraLinha(f"Sistema de alunos"))
# help(mostraLinha)
#

def fatoria(num=1):
    f = 1
    for c in range(1, num+1):
        f *= c
    return f

n = int(input("digie um numero: "))
print(fatoria(n))
