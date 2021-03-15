lista = []

while True:
    n = int(input("Digite um valor: "))
    if n in lista:
        print("Numero repetido. Não vou adicionar")
    else:
        print("Numero adicionado")
        lista.append(n)
    continua = input("Deseja continuar? [s/n]: ").upper()
    if continua == "N":
        break
print("#" *20)
print(f"Você digitou os números {lista}")



