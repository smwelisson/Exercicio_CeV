numeros = [[], []]
for i in range(1, 8):
    add = int(input(f"Digite o {i}º valor: "))
    if add % 2 == 0:
        numeros[0].append(add)
    else:
        numeros[1].append(add)
numeros[0].sort()
numeros[1].sort()
print(f"Os valores pares digitados foram: {numeros[0]}")
print(f"Os valores impares digitados foram: {numeros[1]}")
