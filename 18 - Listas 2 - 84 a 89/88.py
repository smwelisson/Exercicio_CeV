from random import randint
jogos = 5

for quantidade_jogos in range(1, jogos+1):
    mega = []
    while len(mega) < 6:
        num_aleatorios = randint(1, 60)
        if num_aleatorios not in mega:
            mega.append(num_aleatorios)
        mega.sort()
    print(f"Jogos {quantidade_jogos}: {mega}")
