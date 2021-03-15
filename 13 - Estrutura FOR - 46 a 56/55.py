'''leia o peso de 5 pessoas e mostre o maior e o menor'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Digite o peso da {} pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso
print(maior)
print(menor)

'''
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print(maior)'''