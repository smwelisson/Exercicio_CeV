'''Escreva um programa que leia 2 numeros inteiros e diga se
 o primeiro é maior ou o segundo é maior ou se ambos são iguais'''

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
if n1 > n2:
    print("O Primeiro número é maior.")
elif n2 > n1:
    print("O Segundo número é maior.")
else:
    print("Esses números são iguais.")
