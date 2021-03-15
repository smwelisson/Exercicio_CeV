#programa que jogue para ou impar com o computador. o programa só para quando o jogador perder e mostra o total de vitorias consecutivas
#dá pra reduzir
from random import randint
cont = 0
while True:
    pc = randint(0, 10)
    jogador = int(input("Seu número: "))
    p_i = input("Par ou Impar? [P/I] ").upper().strip()[0]
    soma = jogador + pc
    resultado = (pc + jogador) % 2
    if p_i == "I":
        if resultado == 1:
            print(f"Você jogou {jogador} e o computado {pc}, deu {soma} que é IMPAR")
            print("Você ganhou!")
            print("-=" * 10)
        else:
            print(f"Você jogou {jogador} e o computado {pc}, deu {soma} que é PAR")
            print("Você perdeu!")
            break
    if p_i == "P":
        if resultado == 0:
            print(f"Você jogou {jogador} e o computado {pc}, deu {soma} que é PAR")
            print("Você ganhou!")
            print("-=" * 10)
        else:
            print(f"Você jogou {jogador} e o computado {pc}, deu {soma} que é IMPAR")
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")
    cont += 1
print(f"Você ganhou {cont} vezes")