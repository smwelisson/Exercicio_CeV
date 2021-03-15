'''programa que leia 6 numeros inteiros e mostre a soma apenas dos numeros pares'''
soma = 0
cont = 0
for num in range(0, 6):
    cont += 1
    x = int(input(" Digite o {}º número: ".format(cont)))
    if x % 2 == 0:
        soma += x
print(soma)