matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite um numero para [{l}, {c}]: "))

for l in range(3):
    for c in range(3):
        print(f"[ {matriz[l][c]:^5} ]", end="")
    print()


# n1 = 0
# for x1 in range(3):
#     n2 = 0
#     for x2 in range(3):
#         num = int(input(f"Digite um valor para [{n1}, {n2}]: "))
#         n2 += 1
#         matriz.append(num)
#     n1 += 1
#
# print("-="*30)
#
# matricial = 0
# for n in matriz:
#     matricial += 1
#     if matricial == 3:
#         print(f"[ {n} ] \n")
#         matricial = 0
#     else:
#         print(f"[ {n} ] ", end="")
#
#
