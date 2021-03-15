lista = []
listaImp = []
listaPar = []
while True:
    lista.append(int(input("Digite um valor: ")))
    cont = input("Deseja continuar? [S/N] ")
    if cont in "Nn":
        break
for num in lista:
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImp.append(num)
print(f"A lista completa é: {lista}")
print(f"A lista de pares é: {listaPar}")
print(f"A lista de impares é: {listaImp}")
