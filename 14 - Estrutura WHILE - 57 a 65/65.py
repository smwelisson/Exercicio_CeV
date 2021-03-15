"""programa que leia varios numeros e no final mostre a média entre todos os valores e o maior e menor numero.
e depois perguntar se quer ou não continuar digitando valores"""
continuar = "S"
soma = media = quant = maior = menor = 0
while continuar in "S":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = input("Deseja continuar? [S/N] ").strip()[0].upper()
media = soma / quant
print("A media de números digitados foi de {}. O maior número foi {} e o menor foi {}".format(media, maior, menor))