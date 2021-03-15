from random import randint


def sorteia():
    list = []
    for num in range(5):
        list.append(randint(1, 10))
    return list

lista = sorteia()


def somaPar(lista):
    pares = []
    for par in lista:
        if par % 2 == 0:
            pares.append(par)
    print(lista)
    print(f"{pares} e a soma dá {sum(pares)}")

somaPar(lista)