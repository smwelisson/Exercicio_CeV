#programa que simule o funcionamento de um caixa eletronico. pergunte o valor sacado(num int)
# e no final quantas cedulas de cada valor são entregues(50, 20, 10, 1)
print("#" * 17)
print("#  Banco banco  #")
print("#" * 17)
total = int(input("Valor do saque: R$ "))
#total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} de R${ced}")
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break
