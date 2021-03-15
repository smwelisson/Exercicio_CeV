"""programa que leia o termo e a razão e mostre os 10 primeiros numeros da p.a - usando while"""
'''termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
enesimo = termo1 + (10 - 1) * razao

while termo1 != enesimo:
    enesimo = termo1 + (10 - 1) * razao
    print(termo1 + razao, end="")'''

termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 1

while cont <= 10:
    cont += 1
    print(termo1, end=" -> ")
    termo1 += razao
print("Fim")
