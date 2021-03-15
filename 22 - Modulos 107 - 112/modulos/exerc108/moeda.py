def aumento(num, taxa):
    '''teste'''
    return num + (num*(taxa/100))


def diminuir(num, taxa):
    '''teste'''
    return num - (num*(taxa/100))


def dobro(num):
    '''teste'''
    return float(num * 2)


def metade(num):
    '''teste'''
    return float(num / 2)


def moeda(cifrao):
    return f"R${cifrao:.2f}".replace('.', ',')


def resumo():
    pass