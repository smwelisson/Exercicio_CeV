"""Programa que leia varios numeros e só pare quando digitar 999. depois mostre quantos numeros foram digitado
e a soma entre eles"""
'''num = cont = soma = 0
while num != 999:
    num = int(input("Digite outro número ou 999 para sair: "))
    cont += 1
    soma += num
    if num == 999:
        soma -= 999
        cont -= 1
print("Fora digitados {} números e a soma deles é de {}".format(cont, soma))'''

num = cont = soma = 0
num = int(input("Digite outro número ou 999 para sair: "))
while num != 999:
    cont += 1
    soma += num
    num = int(input("Digite outro número ou 999 para sair: "))
print("Fora digitados {} números e a soma deles é de {}".format(cont, soma))