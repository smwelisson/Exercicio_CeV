#Crie um programa que leia varios num int pelo teclado. o programa só vai parar quando o usuario digitar o valor 999
#dizer quantos num foram digitados e a soma entre eles


num = soma = cont = 0
while True:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    soma += num
    cont += 1

print(f"Você digitou {cont} números e a soma de todos foi igual a {soma}")
