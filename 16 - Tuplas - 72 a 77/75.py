num = (1, 4 ,2 ,6)
print("Os valores escolhidos são: ", num)
if 9 in num:
    print(f"O valor 9 aparece {num.count(9)} vezes")
else:
    print("Não tem 9 na lista")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3) + 1}ª posição")
else:
    print("Não tem nenhum 3.")
print(f"Os números pares da tupla são: ", end="")
for ehPar in num:
    if ehPar % 2 == 0:
        print(ehPar, end=" ")
