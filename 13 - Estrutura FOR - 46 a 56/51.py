""" Programa que leia o primeiro termo e a razão de uma progreção aritimetica,
mostrando os 10 primeiros termos dessa PA"""
num = int(input("Informe o primeiro Termo da PA: "))
razao = int(input("Qual a razão da PA? "))
decimo = num + ((10 - 1) * razao)
for c in range(num, decimo + 1, razao):
    print(c, end=" > ")
print("Fim")
