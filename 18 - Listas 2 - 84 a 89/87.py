matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
eh_par = soma_terceira = maior = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("-=" * 30)
for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^4}]", end="")
        if matriz[l][c] % 2 == 0:
            eh_par += matriz[l][c]
        if c == 2:
            soma_terceira += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
    print()
print("-=" * 30)
print(f"Soma dos pares: {eh_par}")
print(f"Soma terceira coluna: {soma_terceira}")
print(f"O maior numero da segunda linha: {maior}")
