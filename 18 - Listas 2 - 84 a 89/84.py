lista = []
dados = []
maior = menor = 0
while True:
    dados.append(input("Nome: "))
    dados.append(int(input("Peso: ")))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    cont = input("Deseja continuar? [S/N]")
    if cont in ("Nn"):
        break
print(f"Ao todo você cadastrou {len(lista)} pessoas")
print(f"O maior peso foi {maior}Kg. Peso de ", end="")
for p in lista:
    if p[1] == maior:
        print(p[0])
print(f"O menor peso foi {menor}Kg. Peso de ", end="")
for p in lista:
    if p[1] == menor:
        print(p[0])
