lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    cont = input("Quer continuar? [s/n]")
    if cont in ("Nn"):
        break

print(f"Você digitou {len(lista)} elementos")
lista.sort(reverse=True)
print(f"os valores em ordem decrescente são {lista}")
if 5 in lista:
    print(f"O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")