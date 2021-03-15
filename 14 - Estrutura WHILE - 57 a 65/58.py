"""Jogo de adivinhação, onde vc vai tentar até acertar"""
from random import randint
pc = randint(1, 10)
print("Seu computador penseu em um numero entre 1 e 10. Consegue adivinhar?")
palpite = 0
tentativas = 0
while palpite != pc:
    palpite = int(input("Seu palpite: "))
    if palpite > pc:
        print("Menos...")
    else:
        print("Mais...")
    tentativas += 1
print("Você Acertou em {} tentativas".format(tentativas))