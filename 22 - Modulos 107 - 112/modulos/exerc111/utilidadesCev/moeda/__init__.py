def aumento(num, taxa=10, form=True):
    '''teste'''
    res = num + (num*(taxa/100))
    return res if form is False else moeda(res)


def diminuir(num, taxa=10, form=True):
    '''teste'''
    res = num - (num*(taxa/100))
    return res if form is False else moeda(res)


def dobro(num, form=True):
    '''teste'''
    res = float(num * 2)
    return res if form is False else moeda(res)


def metade(num, form=True):
    '''teste'''
    res = float(num / 2)
    return res if form is False else moeda(res)


def moeda(valor):
    return f"R${valor:.2f}".replace('.', ',')


def resumo(valor=0, taxa=10):
    print(f"O metade de {moeda(valor)} é {metade(valor, True)}")
    print(f"O dobro de {moeda(valor)} é {dobro(valor, True)}")
    print(f"O aumento de 10% é {aumento(valor, 10, True)}")
