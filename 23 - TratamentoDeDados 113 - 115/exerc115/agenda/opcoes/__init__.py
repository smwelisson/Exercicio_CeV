def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU')
    for op, item in enumerate(lista, start=1):
        print(f"{op} - {item}")
    print(linha())
    opc = leiaInt("Sua opcão: ")
    print(linha())
    return opc

def leiaInt(num):
    valido = False
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print("Erro! Tente novamente")
            continue
        except (KeyboardInterrupt):
            print("\nPrograma encerrado")
            return 0
        else:
            return n


def listar(opcao):
    pass


def cadatrar(nome):
    pass