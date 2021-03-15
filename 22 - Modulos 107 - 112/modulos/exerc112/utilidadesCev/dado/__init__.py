from exerc112.utilidadesCev import moeda

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f"'{entrada}' é um preço invalido")
        else:
            valido = True
            return float(entrada)
