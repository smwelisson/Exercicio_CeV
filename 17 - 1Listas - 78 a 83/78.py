num = []
for add in range(0,5):
    num.append(int(input(f"Digite o {add+1}º numero: ")))
print(f"Os numeros digitados foram: {num}")
print(f"O maior numero digitado foi o {max(num)}. Nas posições: ", end=" ")
for i, num_maximos in enumerate(num):
    if num_maximos == max(num):
        print(f"{i}...", end="")
print("")
print(f"O menor numero digitado foi o {min(num)}. Nas posições: ", end=" ")
for i, num_maximos in enumerate(num):
    if num_maximos == min(num):
        print(f"{i}...", end="")
