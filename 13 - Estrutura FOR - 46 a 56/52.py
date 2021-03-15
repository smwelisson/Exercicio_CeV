'''programa que leia um numero inteiro e diga se é ou nao um numero primo'''
count = 0
num = int(input("Digite um número para saber se é primo: "))
for c in range(1, num + 1):
    if num % c == 0:
        count += 1
if count == 2:
    print("{} foi divisivel somente {} vezes, então é um número primo".format(num, count))
else:
    print("{} foi divisivel {} vezes. Então não é um número primo".format(num, count))
