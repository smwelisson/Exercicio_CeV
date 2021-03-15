'''Crie um programa que mostre os valores PARES entre 1 e 50'''
for pares in range(1, 51):
    if pares % 2 == 0:
        print(pares, end=" ")

print("")

# ou então de forma mais rapida:

for pares2 in range(2, 51, 2):
    print(pares2, end=" ")
