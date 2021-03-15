from agenda.opcoes import cabecalho

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Erro ao criar")
    else:
        print("Arquivo criado")


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("erro ao abrir")
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('erro ao cadastrar')
        else:
            print("Novo registro adicionado")
        finally:
            a.close()
