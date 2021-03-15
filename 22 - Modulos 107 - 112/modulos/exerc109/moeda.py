def aumento(num, taxa=10, form=False):
    '''teste'''
    res = num + (num*(taxa/100))
    return res if form is False else moeda(res)


def diminuir(num, taxa=10, form=False):
    '''teste'''
    res = num - (num*(taxa/100))
    return res if form is False else moeda(res)

def dobro(num, form=False):
    '''teste'''
    res = float(num * 2)
    return res if form is False else moeda(res)

def metade(num, form=False):
    '''teste'''
    res = float(num / 2)
    return res if form is False else moeda(res)

def moeda(valor):
    return f"R${valor:.2f}".replace('.', ',')
