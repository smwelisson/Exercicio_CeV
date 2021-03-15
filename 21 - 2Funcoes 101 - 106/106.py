def ajuda(comando):
    return (help(comando))


comando = input("Digite o comando: ")
while comando != 'fim':
    comando = input("Digite o comando: ")
    print(ajuda(comando))


