'''crie um programa que faça o computador jogar jokenpô com vc '''
#Pode ser simplificado
from random import randint
pc = (randint(1, 3))
print('''Vamos jogar JOKENPÔ!

Escolha entre
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
''')
jogador = int(input("Sua escolha: "))
if jogador == 1 and 2 and 3:
    if jogador == 1:
        if pc == 1:
            print("Ambos colocaram Pedra \n Deu empate")
        elif pc == 2:
            print("Você colocou Pedra \n Computador Papel \n Você perdeu")
        elif pc == 3:
            print("Você colocou Pedra \n Computador Tesoura \n Você ganhou")
    if jogador == 2:
        if pc == 2:
            print("Ambos colocaram Papel \n Deu empate")
        elif pc == 1:
            print("Você colocou Papel \n Computador Pedra \n Você ganhou")
        elif pc == 3:
            print("Você colocou Papel \n Computador Tesoura \n Você perdeu")
    if jogador == 3:
        if pc == 3:
            print("Ambos colocaram Tesoura \n Deu empate")
        elif pc == 1:
            print("Você colocou Tesoura \n Computador Pedra \n Você perdeu")
        elif pc == 2:
            print("Você colocou Tesoura \n Computador Papel \n Você ganhou")
#não vai dar certo assim. pq? não sei. Tem que colocar o else em cada 'if jogador'
else:
    print("Comando invalido")





#forma simplificada incompleta
from time import sleep
from random import randint
intes = ("Pedra", "Papel", "Tesoura")
pc = randint(0, 2)
print('''Vamos jogar JOKENPÔ!

Escolha entre
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input("Sua escolha: "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

print("-=" * 15)
print("O Computador escolheu {}".format(intes[pc]))
print("O Jogador escolheu {}".format(intes[jogador]))
print("-=" * 15)
