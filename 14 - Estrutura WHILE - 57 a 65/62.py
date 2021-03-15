"""melhore o desafio 61, perguntando se o usuario quer mais termos, o programa acaba quando mostrar 0 termos"""
termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        cont += 1
        print(termo1, end=" -> ")
        termo1 += razao
    print("Pausa")
    mais = int(input("Quantos termo você quer mostrar a mais? "))
print("Finalizado com {} termos mostrados".format(total))